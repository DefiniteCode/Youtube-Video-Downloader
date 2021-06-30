import pytube
import tkinter
from tkinter import *
import tkinter.messagebox



class downloader():
    def __init__(self,root):
        self.root = root
        self.root.title('Youtube Video Downloader')
        self.root.geometry('400x500+15+15')
        self.root.configure(bg='light blue')
       

        #=============================================================Frames========================================================

        self.frame1 = Frame(self.root,width=380, height=350, bg='white')
        self.frame1.place(x=10,y=100)

        self.frame2 =  Frame(self.root,width=360, height=55, bg='#df2800')
        self.frame2.place(x=20,y=280)

        self.show = Label(self.frame1,text='',font=('Arial',11,'bold'),fg='green',bg='white')
        self.show.place(x=80,y=245)

        Label(self.frame2,text='Paste link here:',font=('Arial',12,'bold'),bg='#df2800',fg='white').place(x=0,y=0)
        self.link = Entry(self.frame2,width=38,font=('Arial',13))
        self.link.place(x=5,y=30)



        #==========================================================Functions==========================================================

        def paste():
            self.link.event_generate('<Control-v>')

        def start():
            try:
                #check if the client pasted a link
                if self.link.get() == '':
                    tkinter.messagebox.showerror('Empty Link','Please paste a link to download')
                else:
                    
                    #if a link is found you can now download
                    video_url = self.link.get()
                    youtube = pytube.YouTube(video_url)
                    video = youtube.streams.first()
                    video.download()
                    self.show.config(text='Video Download Completed!!!')

            except:
                text = ''' Oops, A problem was encountered, check the link you pasted or Please check your internet connection
                    

                        '''
                tkinter.messagebox.showerror('Error',text)



        #=====================================Other widgets= Labels,Buttons,Entry======================================================

        Label(root,text='Youtube Video Downloader',font=('calibri',24,'bold'),fg='green',bg='light blue').place(x=15,y=0)
        Label(root,text='Programmed By: Wumpini',font=('calibri',14,'bold'),fg='green',bg='light blue').place(x=80,y=35)

        
        Label(self.frame1,text='________',font=('Arial',12,'bold'),bg='white').place(x=145,y=22)
        Label(self.frame1,text='Steps',font=('Arial',18,'bold'),bg='white').place(x=150,y=5)
        
        self.text1 = '1.Goto Youtube and copy the URL of the video'
        self.text2 = '2.Paste it in the space provided below'
        self.text3 = '3.Click on the download button'
        self.text4 = '4.Wait while it downloads'

        Label(self.frame1,text=self.text1,font=('Arial',11,'bold'), bg='white').place(x=0,y=60)
        Label(self.frame1,text=self.text2,font=('Arial',11,'bold'), bg='white').place(x=0,y=80)
        Label(self.frame1,text=self.text3,font=('Arial',11,'bold'), bg='white').place(x=0,y=100)
        Label(self.frame1,text=self.text4,font=('Arial',11,'bold'), bg='white').place(x=0,y=120)

        
        

        Button(self.frame1,text='Download',font=('Arial',12,'bold'),fg='white',bg='red',command=start).place(x=70,y=280)
        Button(self.frame1,text='Paste',width=9,font=('Arial',12,'bold'),fg='white',bg='red',command=paste).place(x=200,y=280)

        Label(self.root,text='Copyright:wumpinisuleman@gmail.com',font=('Arial',11,'bold'),fg='blue',bg='light blue').place(x=50,y=460)



        






root = Tk()
ob = downloader(root)
root.mainloop()
