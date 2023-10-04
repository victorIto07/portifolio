import requests
import json
from io import BytesIO
import pygame
import spotipy
import spotipy.util as util
from colorthief import ColorThief
import os

class Colors:
    black = "#000000"
    acc_white = "#ffffff"
    green = "#1DB954"
    grey = "#052510"
    white = "#f1f1f1"
    light_grey = "#b3b3b3"

pygame.init()

SONG_NAME = 0
SONG_IMG = 1
SONG_ARTIST = 2
SONG_PROGRESS = 3
SONG_TOTAL_TIME = 4
SONG_ID = 5
SONG_IS_PAUSED = 6

IMG_PADDING = 125

LINE_PADDING = 110
LINE_WIDTH = 11

COLORS = Colors()

TOKEN_CURRENT_PLAYING = 0
TOKEN_CHANGE_SONG = 1
TOKEN_PLAYBACK_STATE = 2

class Main:
    WIDTH, HEIGHT = 700,700
    FONT_BIG = pygame.font.Font("assets/fonts/GothamBold.ttf",45)
    FONT_SMOL = pygame.font.Font("assets/fonts/GothamLight.ttf",20)
    CLOCK = pygame.time.Clock()
    client_id = "092351a7378c4ef388ff08a1061f0ebb"
    client_secret = "527c405d956b4333ab9f238823f9fbf7"
    redirect_uri = "http://localhost/redirect"
    current_song = [None,None,None,None,None,None,None]
    tokens = [None, None, None]
    f_count = 0

    def __init__(self):
        self.getCredentials()
        self.getTokens()
        self.createDisplay()
        self.loadImages()
        self.getCurrentTrack()
        self.running = True
        self.getDevices()
        while self.running:
            self.CLOCK.tick(30)
            self.getEvents()
            if self.f_count % 45 == 0:
                self.getCurrentTrack()
            self.f_count += 1
        pygame.quit()

    def getTokens(self):
        self.getUserToken('user-read-currently-playing')
        self.getUserToken('user-read-playback-state')
        self.getUserToken('user-modify-playback-state')

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_pause()
                if event.key == pygame.K_DOWN:
                    self.createDisplay()
                    self.updateSong()
                if event.key == pygame.K_RIGHT:
                    self.nextSong()
                if event.key == pygame.K_LEFT:
                    self.previousSong()

    def loadImages(self):
        self.icon = pygame.image.load("assets/spotify.png")
        pygame.display.set_icon(self.icon)
        self.img_paused = pygame.transform.scale(pygame.image.load("assets/paused.png").convert_alpha(),(120,120))
        self.img_paused_pos = (self.WIDTH/2-self.img_paused.get_width()/2,self.HEIGHT/2-self.img_paused.get_height()/2)

    def createDisplay(self):
        self.COVER_SIZE = self.WIDTH-IMG_PADDING*2
        self.pg_y = self.HEIGHT-75
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("spotivi(tuitu)")
        self.layer = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.layer.set_alpha(230)
        self.layer.fill("#000000")
        self.no_song_t = self.FONT_BIG.render("No song playing.. :(", True, COLORS.white)
        self.no_song_t_pos = (self.WIDTH/2-self.no_song_t.get_width()/2, self.HEIGHT/2-self.no_song_t.get_height()/2)

    def getCredentials(self):
        credentials = json.loads(requests.post("https://accounts.spotify.com/api/token", headers={"Content-Type":"application/x-www-form-urlencoded"}, data={"grant_type":"client_credentials","client_id":self.client_id, "client_secret":self.client_secret}).text)
        self.myHeader = {"Authorization": f'{credentials["token_type"]} {credentials["access_token"]}'}

    def getArtistData(self, artist_id):
        req = json.loads(requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=self.myHeader, data={"grant_type":"user-read-recently-played"}).text)
        with open(f"assets/{req['name']}.jpg","wb") as img:
            img.write(requests.get(req["images"][0]["url"]).content)
            img.close()
        return req
    
    def getUserToken(self, scope):
        if scope=='user-read-currently-playing' and os.path.exists('tokens/TOKEN_CURRENT_PLAYING.json'):
            with open('tokens/TOKEN_CURRENT_PLAYING.json') as t:
                self.tokens[TOKEN_CURRENT_PLAYING] = t.read()
                t.close()
            return
        if scope=='user-modify-playback-state' and os.path.exists('tokens/TOKEN_CHANGE_SONG.json'):
            with open('tokens/TOKEN_CHANGE_SONG.json') as t:
                self.tokens[TOKEN_CHANGE_SONG] = t.read()
                t.close()
            return
        if scope=='user-read-playback-state' and os.path.exists('tokens/TOKEN_PLAYBACK_STATE.json'):
            with open('tokens/TOKEN_PLAYBACK_STATE.json') as t:
                self.tokens[TOKEN_PLAYBACK_STATE] = t.read()
                t.close()
            return
        token = util.prompt_for_user_token('victor.m.ito', scope, client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri)
        if scope == 'user-read-currently-playing':
            self.tokens[TOKEN_CURRENT_PLAYING] = token
            with open('tokens/TOKEN_CURRENT_PLAYING.json', 'w') as t:
                t.write(token)
                t.close()
        if scope == 'user-modify-playback-state':
            self.tokens[TOKEN_CHANGE_SONG] = token
            with open('tokens/TOKEN_CHANGE_SONG.json', 'w') as t:
                t.write(token)
                t.close()
        if scope == 'user-read-playback-state':
            self.tokens[TOKEN_PLAYBACK_STATE] = token
            with open('tokens/TOKEN_PLAYBACK_STATE.json', 'w') as t:
                t.write(token)
                t.close()

    def getDevices(self):
        sp = spotipy.Spotify(auth=self.tokens[TOKEN_PLAYBACK_STATE])
        self.devices = sp.devices()["devices"]

    def getCurrentTrack(self):
        sp = spotipy.Spotify(auth=self.tokens[TOKEN_CURRENT_PLAYING])
        result = sp.current_user_playing_track()
        if result is None:
            if self.current_song[SONG_ID]:
                self.current_song[SONG_NAME] = None
                self.current_song[SONG_IMG] = None
                self.current_song[SONG_ARTIST] = None
                self.current_song[SONG_PROGRESS] = None
                self.current_song[SONG_TOTAL_TIME] = None
                self.current_song[SONG_ID] = None
                self.current_song[SONG_IS_PAUSED] = None
                self.WIN.fill(COLORS.black)
            self.WIN.blit(self.no_song_t, self.no_song_t_pos)
        else:  
            self.current_song[SONG_PROGRESS] = result["progress_ms"]
            self.current_song[SONG_TOTAL_TIME] = result["item"]["duration_ms"]
            c_paused = result["is_playing"] != self.current_song[SONG_IS_PAUSED]
            self.current_song[SONG_IS_PAUSED] = not result["is_playing"]
            if self.current_song[SONG_ID] == None or result["item"]["id"] != self.current_song[SONG_ID]:
                self.current_song[SONG_NAME] = result["item"]["name"]
                self.current_song[SONG_ARTIST] = result["item"]["artists"][0]["name"]
                self.current_song[SONG_IMG] = result["item"]["album"]["images"][0]["url"]
                self.current_song[SONG_ID] = result["item"]["id"]
                img = pygame.image.load(BytesIO(requests.get(self.current_song[SONG_IMG]).content))
                self.song_cover = pygame.transform.scale(img, (self.COVER_SIZE,self.COVER_SIZE))
                size = self.song_cover.get_size()
                self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
                pygame.draw.rect(self.rect_image, COLORS.acc_white, (0, 0, *size), border_radius=10)
                self.image = self.song_cover.copy().convert_alpha()
                self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN) 
                self.song_cover_bg = pygame.transform.scale(img, (self.WIDTH,self.HEIGHT))
                self.song_name_shadow = self.FONT_BIG.render(self.current_song[SONG_NAME][:20]+"..." if len(self.current_song[SONG_NAME])>23 else self.current_song[SONG_NAME], True, COLORS.grey)
                self.song_name = self.FONT_BIG.render(self.current_song[SONG_NAME][:20]+"..." if len(self.current_song[SONG_NAME])>23 else self.current_song[SONG_NAME], True, COLORS.white)
                self.song_name_pos = (self.WIDTH/2-self.song_name.get_width()/2, self.HEIGHT-170)
                self.artist_name_shadow = self.FONT_SMOL.render(self.current_song[SONG_ARTIST][:20]+"..." if len(self.current_song[SONG_ARTIST])>23 else self.current_song[SONG_ARTIST], True, COLORS.grey)
                self.artist_name = self.FONT_SMOL.render(self.current_song[SONG_ARTIST][:20]+"..." if len(self.current_song[SONG_ARTIST])>23 else self.current_song[SONG_ARTIST], True, COLORS.light_grey)
                self.artist_name_pos = (self.WIDTH/2-self.artist_name.get_width()/2, self.HEIGHT-122)
                self.updateSong()
            elif c_paused:
                self.updateSong()
            self.drawLine()
        pygame.display.update()
        
    def updateSong(self):
        self.WIN.blit(self.song_cover_bg, (0,0))
        self.WIN.blit(self.layer, (0,0))
        self.WIN.blit(self.image, (IMG_PADDING,self.song_name_pos[1] - 35 - self.COVER_SIZE))
        self.WIN.blit(self.song_name_shadow, (self.song_name_pos[0] + 5,self.song_name_pos[1] + 5))
        self.WIN.blit(self.song_name, self.song_name_pos)
        # self.WIN.blit(self.artist_name_shadow, (self.artist_name_pos[0] + 5, self.artist_name_pos[1] + 5))
        self.WIN.blit(self.artist_name, self.artist_name_pos)
        if self.current_song[SONG_IS_PAUSED]:
            self.WIN.blit(self.layer, (0,0))
            self.WIN.blit(self.img_paused, self.img_paused_pos)


    def drawLine(self):
        if not self.current_song[SONG_ID]:
            return
        pygame.draw.rect(self.WIN, COLORS.white, (LINE_PADDING, self.pg_y, self.WIDTH-(LINE_PADDING*2), LINE_WIDTH),0, (LINE_WIDTH//2)-1)
        pygame.draw.rect(self.WIN, COLORS.green, (LINE_PADDING, self.pg_y, (self.WIDTH - (LINE_PADDING*2)) * (self.current_song[SONG_PROGRESS]/self.current_song[SONG_TOTAL_TIME]), LINE_WIDTH),0, (LINE_WIDTH//2)-1)        

    def nextSong(self):
        self.getDevices()
        d = [i for i in self.devices if i["is_active"]]
        if not len(d):
            return
        sp = spotipy.Spotify(auth=self.tokens[TOKEN_CHANGE_SONG])
        sp.next_track(d[0]["id"])
        self.getCurrentTrack()

    def previousSong(self):
        self.getDevices()
        d = [i for i in self.devices if i["is_active"]]
        if not len(d):
            return
        sp = spotipy.Spotify(auth=self.tokens[TOKEN_CHANGE_SONG])
        sp.previous_track(d[0]["id"])
        self.getCurrentTrack()

    def start_pause(self):
        sp = spotipy.Spotify(auth=self.tokens[TOKEN_CHANGE_SONG])
        if self.current_song[SONG_IS_PAUSED]:
            self.current_song[SONG_IS_PAUSED] = False
            sp.start_playback()
        else:
            self.current_song[SONG_IS_PAUSED] = True
            sp.pause_playback()
        self.updateSong()
    
Main()