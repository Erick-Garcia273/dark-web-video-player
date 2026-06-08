#!/usr/bin/env python3
"""
Enhanced Video Manager with Ad Blocking
Integrates ad blocker into video manager
"""

import os
import json
import subprocess
import threading
from datetime import datetime
from pathlib import Path
import yt_dlp
from config import SETTINGS
import requests
from ad_blocker import AdBlocker, YouTubeAdRemover, AdFreeStreamHandler

class VideoManager:
    def __init__(self):
        self.download_dir = SETTINGS["download_dir"]
        self.audio_dir = SETTINGS["audio_dir"]
        self.history_file = SETTINGS["history_file"]
        self.favorites_file = SETTINGS["favorites_file"]
        self.playlists_file = SETTINGS["playlists_file"]
        self.searches_file = SETTINGS["searches_file"]
        self.incognito_mode = False
        self.proxy_url = None
        
        # Initialize ad blocker
        self.ad_blocker = AdBlocker()
        self.ad_free_handler = AdFreeStreamHandler()
        self.ads_blocked_count = 0
        
        self._ensure_dirs()
        
    def _ensure_dirs(self):
        Path(self.download_dir).mkdir(parents=True, exist_ok=True)
        Path(self.audio_dir).mkdir(parents=True, exist_ok=True)
        Path(os.path.dirname(self.history_file)).mkdir(parents=True, exist_ok=True)
        
    def set_incognito_mode(self, enabled):
        self.incognito_mode = enabled
        
    def set_proxy(self, proxy_url):
        self.proxy_url = proxy_url
    
    def test_connection(self):
        try:
            response = requests.get('https://www.google.com', timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_video_info(self, url):
        try:
            ydl_opts = self.ad_free_handler.prepare_download_options(url)
            ydl_opts['quiet'] = True
            ydl_opts['no_warnings'] = True
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'thumbnail': info.get('thumbnail'),
                    'channel': info.get('uploader'),
                    'views': info.get('view_count'),
                    'description': info.get('description'),
                    'upload_date': info.get('upload_date'),
                    'url': url,
                }
        except Exception as e:
            raise Exception(f"Error getting video info: {str(e)}")
    
    def download_video(self, url, callback=None, audio_only=False, subtitle=False):
        try:
            if audio_only:
                return self.download_audio(url, callback)
            
            # Get ad-free download options
            ydl_opts = self.ad_free_handler.prepare_download_options(url, audio_only=False)
            
            ydl_opts['outtmpl'] = os.path.join(self.download_dir, '%(title)s.%(ext)s')
            ydl_opts['quiet'] = False
            ydl_opts['no_warnings'] = False
            ydl_opts['progress_hooks'] = [callback] if callback else []
            ydl_opts['writesubtitles'] = subtitle
            
            if subtitle:
                ydl_opts['subtitle'] = 'en'
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
                # Track blocked ads
                self.ads_blocked_count += 1
                
                return filename
        except Exception as e:
            raise Exception(f"Error downloading video: {str(e)}")
    
    def download_audio(self, url, callback=None):
        try:
            ydl_opts = self.ad_free_handler.prepare_download_options(url, audio_only=True)
            
            ydl_opts['outtmpl'] = os.path.join(self.audio_dir, '%(title)s.%(ext)s')
            ydl_opts['quiet'] = False
            ydl_opts['no_warnings'] = False
            ydl_opts['progress_hooks'] = [callback] if callback else []
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                return filename
        except Exception as e:
            raise Exception(f"Error downloading audio: {str(e)}")
    
    def download_playlist(self, url, callback=None, audio_only=False):
        try:
            ydl_opts = self.ad_free_handler.prepare_download_options(url, audio_only=audio_only)
            
            ydl_opts['outtmpl'] = os.path.join(
                self.audio_dir if audio_only else self.download_dir,
                '%(playlist_title)s/%(title)s.%(ext)s'
            )
            ydl_opts['quiet'] = False
            ydl_opts['no_warnings'] = False
            ydl_opts['progress_hooks'] = [callback] if callback else []
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return f"Downloaded {info.get('_type')} successfully"
        except Exception as e:
            raise Exception(f"Error downloading playlist: {str(e)}")
    
    def search_videos(self, query, max_results=15):
        try:
            self.add_to_searches(query)
            
            ydl_opts = self.ad_free_handler.prepare_download_options(f"ytsearch:{query}")
            ydl_opts['quiet'] = True
            ydl_opts['no_warnings'] = True
            ydl_opts['extract_flat'] = 'in_playlist'
            ydl_opts['playlistend'] = max_results
            
            search_url = f"ytsearch{max_results}:{query}"
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(search_url, download=False)
                
                videos = []
                for entry in info.get('entries', []):
                    videos.append({
                        'title': entry.get('title'),
                        'url': entry.get('url'),
                        'id': entry.get('id'),
                        'channel': entry.get('uploader'),
                        'duration': entry.get('duration'),
                    })
                return videos
        except Exception as e:
            raise Exception(f"Error searching videos: {str(e)}")
    
    # PLAYLISTS
    def create_playlist(self, name, description=""):
        playlists = self._load_json(self.playlists_file, {})
        if name not in playlists:
            playlists[name] = {
                'name': name,
                'description': description,
                'videos': [],
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
            }
            self._save_json(self.playlists_file, playlists)
            return True
        return False
    
    def get_playlists(self):
        return self._load_json(self.playlists_file, {})
    
    def add_to_playlist(self, playlist_name, video_data):
        playlists = self._load_json(self.playlists_file, {})
        if playlist_name in playlists:
            if not any(v.get('url') == video_data.get('url') for v in playlists[playlist_name]['videos']):
                playlists[playlist_name]['videos'].append(video_data)
                playlists[playlist_name]['updated_at'] = datetime.now().isoformat()
                self._save_json(self.playlists_file, playlists)
                return True
        return False
    
    def delete_playlist(self, playlist_name):
        playlists = self._load_json(self.playlists_file, {})
        if playlist_name in playlists:
            del playlists[playlist_name]
            self._save_json(self.playlists_file, playlists)
            return True
        return False
    
    def get_playlist_videos(self, playlist_name):
        playlists = self._load_json(self.playlists_file, {})
        if playlist_name in playlists:
            return playlists[playlist_name]['videos']
        return []
    
    # EXPORT/IMPORT
    def export_playlist(self, playlist_name, format='json'):
        playlists = self._load_json(self.playlists_file, {})
        if playlist_name not in playlists:
            return None
        
        playlist = playlists[playlist_name]
        
        if format == 'json':
            filename = f"{playlist_name}_playlist.json"
            filepath = os.path.join(self.download_dir, filename)
            self._save_json(filepath, playlist)
            return filepath
        
        elif format == 'm3u':
            filename = f"{playlist_name}_playlist.m3u"
            filepath = os.path.join(self.download_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("#EXTM3U\n")
                for video in playlist['videos']:
                    f.write(f"#EXTINF:-1,{video.get('title', 'Unknown')}\n")
                    f.write(f"{video.get('url', '')}\n")
            return filepath
    
    def import_playlist(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'name' in data and 'videos' in data:
                playlists = self._load_json(self.playlists_file, {})
                name = data['name']
                if name not in playlists:
                    playlists[name] = data
                    self._save_json(self.playlists_file, playlists)
                    return True
            return False
        except Exception as e:
            raise Exception(f"Error importing playlist: {str(e)}")
    
    # HISTORY & FAVORITES
    def add_to_history(self, video_data):
        if self.incognito_mode:
            return
        history = self._load_json(self.history_file, [])
        history = [v for v in history if v.get('url') != video_data.get('url')]
        video_data['timestamp'] = datetime.now().isoformat()
        history.insert(0, video_data)
        history = history[:SETTINGS["max_history"]]
        self._save_json(self.history_file, history)
    
    def get_history(self):
        return self._load_json(self.history_file, [])
    
    def clear_history(self):
        self._save_json(self.history_file, [])
    
    def add_to_favorites(self, video_data):
        favorites = self._load_json(self.favorites_file, [])
        if not any(v.get('url') == video_data.get('url') for v in favorites):
            video_data['added_at'] = datetime.now().isoformat()
            favorites.insert(0, video_data)
            self._save_json(self.favorites_file, favorites)
    
    def get_favorites(self):
        return self._load_json(self.favorites_file, [])
    
    def is_favorite(self, url):
        favorites = self._load_json(self.favorites_file, [])
        return any(v.get('url') == url for v in favorites)
    
    # SEARCHES
    def add_to_searches(self, query):
        searches = self._load_json(self.searches_file, [])
        searches = [s for s in searches if s.get('query') != query]
        searches.insert(0, {'query': query, 'timestamp': datetime.now().isoformat()})
        searches = searches[:50]
        self._save_json(self.searches_file, searches)
    
    def get_search_history(self):
        return self._load_json(self.searches_file, [])
    
    def clear_search_history(self):
        self._save_json(self.searches_file, [])
    
    # PLAYBACK
    def play_video(self, filepath):
        try:
            if os.name == 'nt':
                os.startfile(filepath)
            elif os.name == 'posix':
                subprocess.Popen(['open', filepath])
        except Exception as e:
            raise Exception(f"Error playing video: {str(e)}")
    
    # LIBRARY
    def get_downloaded_videos(self):
        if not os.path.exists(self.download_dir):
            return []
        
        videos = []
        for file in os.listdir(self.download_dir):
            if file.endswith(('.mp4', '.mkv', '.webm', '.avi')):
                filepath = os.path.join(self.download_dir, file)
                try:
                    videos.append({
                        'filename': file,
                        'filepath': filepath,
                        'size': os.path.getsize(filepath),
                        'modified': datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
                    })
                except:
                    pass
        return sorted(videos, key=lambda x: x['modified'], reverse=True)
    
    def get_downloaded_audio(self):
        if not os.path.exists(self.audio_dir):
            return []
        
        audio = []
        for file in os.listdir(self.audio_dir):
            if file.endswith(('.mp3', '.m4a', '.wav', '.flac')):
                filepath = os.path.join(self.audio_dir, file)
                try:
                    audio.append({
                        'filename': file,
                        'filepath': filepath,
                        'size': os.path.getsize(filepath),
                        'modified': datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
                    })
                except:
                    pass
        return sorted(audio, key=lambda x: x['modified'], reverse=True)
    
    def delete_downloaded_video(self, filepath):
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except Exception as e:
            raise Exception(f"Error deleting video: {str(e)}")
        return False
    
    def get_library_stats(self):
        videos = self.get_downloaded_videos()
        audio = self.get_downloaded_audio()
        total_video_size = sum(v['size'] for v in videos)
        total_audio_size = sum(a['size'] for a in audio)
        total_size = total_video_size + total_audio_size
        
        return {
            'total_videos': len(videos),
            'total_audio': len(audio),
            'total_items': len(videos) + len(audio),
            'video_size_gb': total_video_size / 1024 / 1024 / 1024,
            'audio_size_gb': total_audio_size / 1024 / 1024 / 1024,
            'total_size_gb': total_size / 1024 / 1024 / 1024,
        }
    
    def get_ad_blocking_stats(self):
        """Get ad blocking statistics"""
        return {
            'ads_blocked': self.ads_blocked_count,
            'blocked_domains': self.ad_blocker.get_blocklist_stats()['blocked_domains'],
        }
    
    # JSON
    @staticmethod
    def _load_json(filepath, default=None):
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return default or {}
    
    @staticmethod
    def _save_json(filepath, data):
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
