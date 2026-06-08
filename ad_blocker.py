#!/usr/bin/env python3
"""
Ad Blocker Module for Dark Web Video Player
Blocks ads from YouTube, Twitch, and other streaming platforms
"""

import re
import json
from urllib.parse import urlparse, parse_qs
from config import SETTINGS

class AdBlocker:
    """Advanced ad blocking system"""
    
    def __init__(self):
        self.blocked_domains = set()
        self.blocked_patterns = []
        self.blocked_urls = set()
        self.load_blocklist()
        
    def load_blocklist(self):
        """Load ad blocking list"""
        # YouTube ad domains
        youtube_ad_domains = [
            'ads.google.com',
            'pagead2.googlesyndication.com',
            'googleads.g.doubleclick.net',
            'adservice.google.com',
            'ad.doubleclick.net',
            'doubleclick.net',
            'www.youtube.com/api/timedtext_proxy',
            'www.youtube.com/ptracking',
            'www.youtube-nocookie.com',
            'youtube.com/watch_ads',
            'youtube.com/ads',
            'youtube-ui.l.google.com',
        ]
        
        # General ad domains
        general_ad_domains = [
            'ads.yahoo.com',
            'ads.microsoft.com',
            'ads.facebook.com',
            'analytics.google.com',
            'google-analytics.com',
            'doubleclick.net',
            'adnxs.com',
            'pubmatic.com',
            'criteo.com',
            'rubiconproject.com',
            'openx.com',
            'lijit.com',
            'contextweb.com',
            'advertising.com',
            'fastclick.net',
            'aggressive.avast.com',
        ]
        
        self.blocked_domains = set(youtube_ad_domains + general_ad_domains)
        
        # Regex patterns for ad URLs
        self.blocked_patterns = [
            r'.*ads?.*',
            r'.*banner.*',
            r'.*advertisement.*',
            r'.*tracking.*',
            r'.*analytics.*',
            r'.*doubleclick.*',
            r'.*googlesyndication.*',
            r'.*pagead.*',
            r'.*adsense.*',
            r'.*adserver.*',
        ]
    
    def is_ad_url(self, url):
        """Check if URL is an ad URL"""
        if not url:
            return False
        
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Check against blocked domains
            for blocked_domain in self.blocked_domains:
                if blocked_domain in domain:
                    return True
            
            # Check against patterns
            url_lower = url.lower()
            for pattern in self.blocked_patterns:
                if re.match(pattern, url_lower):
                    return True
            
            return False
        except:
            return False
    
    def block_youtube_ads(self, ydl_opts):
        """Modify yt-dlp options to skip ads"""
        # Skip ads by using specific format options
        ydl_opts['skip_unavailable_fragments'] = True
        ydl_opts['socket_timeout'] = 30
        
        # Add custom headers to avoid ad injection
        ydl_opts['http_headers'] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # Use sponsorblock to skip sponsored segments
        try:
            ydl_opts['sponsorblock_chapters'] = ['sponsor', 'intro', 'outro', 'selfpromo', 'preview']
        except:
            pass
        
        return ydl_opts
    
    def filter_response(self, response_text):
        """Filter HTML response to remove ads"""
        if not response_text:
            return response_text
        
        # Remove common ad scripts
        ad_patterns = [
            r'<script[^>]*src="[^"]*ads?[^"]*"[^>]*></script>',
            r'<script[^>]*src="[^"]*doubleclick[^"]*"[^>]*></script>',
            r'<script[^>]*src="[^"]*analytics[^"]*"[^>]*></script>',
            r'<script[^>]*src="[^"]*tracking[^"]*"[^>]*></script>',
            r'<ins[^>]*class="[^"]*ad[^"]*"[^>]*>.*?</ins>',
            r'<div[^>]*id="[^"]*ad[^"]*"[^>]*>.*?</div>',
            r'<iframe[^>]*src="[^"]*ads?[^"]*"[^>]*></iframe>',
        ]
        
        filtered = response_text
        for pattern in ad_patterns:
            filtered = re.sub(pattern, '', filtered, flags=re.IGNORECASE | re.DOTALL)
        
        return filtered
    
    def create_ad_free_url(self, original_url):
        """Create ad-free version of URL"""
        try:
            # For YouTube, use different approaches
            if 'youtube.com' in original_url or 'youtu.be' in original_url:
                # Return as-is, yt-dlp will handle ad removal
                return original_url
            
            # For other platforms, remove ad parameters
            parsed = urlparse(original_url)
            params = parse_qs(parsed.query)
            
            # Remove common ad tracking parameters
            ad_params = [
                'utm_source', 'utm_medium', 'utm_campaign', 'utm_content',
                'utm_term', 'gclid', 'fbclid', 'msclkid', 'tracking_id',
                'ad_id', 'adset_id', 'campaign_id', 'source', 'medium',
            ]
            
            for param in ad_params:
                params.pop(param, None)
            
            # Reconstruct URL without ad params
            new_query = '&'.join([f"{k}={v[0]}" for k, v in params.items()])
            
            return f"{parsed.scheme}://{parsed.netloc}{parsed.path}{'?' + new_query if new_query else ''}"
        except:
            return original_url
    
    def get_blocklist_stats(self):
        """Get statistics about blocked domains"""
        return {
            'blocked_domains': len(self.blocked_domains),
            'blocked_patterns': len(self.blocked_patterns),
            'total_blocked': len(self.blocked_domains) + len(self.blocked_patterns),
        }
    
    def update_blocklist(self, new_domains):
        """Update blocklist with new domains"""
        if isinstance(new_domains, list):
            self.blocked_domains.update(new_domains)
        elif isinstance(new_domains, str):
            self.blocked_domains.add(new_domains)
    
    def save_blocklist(self, filepath):
        """Save blocklist to file"""
        data = {
            'blocked_domains': list(self.blocked_domains),
            'blocked_patterns': self.blocked_patterns,
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def load_custom_blocklist(self, filepath):
        """Load custom blocklist from file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.blocked_domains.update(data.get('blocked_domains', []))
                self.blocked_patterns.extend(data.get('blocked_patterns', []))
                return True
        except:
            return False


class YouTubeAdRemover:
    """Specialized YouTube ad removal"""
    
    @staticmethod
    def extract_clean_video_id(url):
        """Extract video ID from URL"""
        patterns = [
            r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
            r'youtu\.be/([a-zA-Z0-9_-]{11})',
            r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    @staticmethod
    def get_ad_free_ydl_options():
        """Get yt-dlp options optimized for ad removal"""
        return {
            'format': 'best[ext=mp4]/best',
            'quiet': False,
            'no_warnings': False,
            'skip_unavailable_fragments': True,
            'socket_timeout': 30,
            'extractor_args': {
                'youtube': {
                    'skip': ['hls', 'dash'],
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
            },
        }
    
    @staticmethod
    def skip_sponsorblock_segments(ydl_opts):
        """Add SponsorBlock support to skip ads and intros"""
        try:
            ydl_opts['sponsorblock_chapters'] = [
                'sponsor',
                'intro',
                'outro',
                'selfpromo',
                'preview',
                'filler',
                'interaction',
                'music_offtopic'
            ]
        except:
            pass
        
        return ydl_opts


class AdFreeStreamHandler:
    """Handle ad-free streaming"""
    
    def __init__(self):
        self.ad_blocker = AdBlocker()
        self.youtube_remover = YouTubeAdRemover()
        self.ads_blocked_count = 0
        self.ads_blocked_bytes = 0
    
    def prepare_download_options(self, url, audio_only=False):
        """Prepare yt-dlp options with ad blocking"""
        
        if 'youtube' in url.lower() or 'youtu.be' in url.lower():
            # Use YouTube-specific ad removal
            ydl_opts = self.youtube_remover.get_ad_free_ydl_options()
            ydl_opts = self.youtube_remover.skip_sponsorblock_segments(ydl_opts)
        else:
            # Use general ad blocker
            ydl_opts = self.ad_blocker.block_youtube_ads({})
        
        # Audio only option
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        
        return ydl_opts
    
    def get_stats(self):
        """Get ad blocking statistics"""
        return {
            'ads_blocked': self.ads_blocked_count,
            'bytes_saved': self.ads_blocked_bytes,
            'bytes_saved_mb': self.ads_blocked_bytes / 1024 / 1024,
            'bytes_saved_gb': self.ads_blocked_bytes / 1024 / 1024 / 1024,
        }
    
    def reset_stats(self):
        """Reset ad blocking statistics"""
        self.ads_blocked_count = 0
        self.ads_blocked_bytes = 0
