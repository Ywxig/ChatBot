import CuteON

class Web_page:

    def Update(listBot="ListBot.sws", file_update="profile.html"):
        list = CuteON.Get_.getAll(listBot)
        for i in list:
            Token = CuteON.Get_.getLine(str(i[0]), "Token")
            Name = CuteON.Get_.getLine(str(i[0]), "Name")
            Description = CuteON.Get_.getLine(str(i[0]), "Description")
            Ava = CuteON.Get_.getLine(str(i[0]), "Ava")
            URL = CuteON.Get_.getLine(str(i[0]), "URL")
            TG = CuteON.Get_.getLine(str(i[0]), "TG")
            DS = CuteON.Get_.getLine(str(i[0]), "DS")
            id = CuteON.Get_.getLine(str(i[0]), "id")

        body = open(file_update, "r", encoding="utf-8")
        B = (body.read()).split("<cut>")
        print(B)
        file = open(file_update, "w", encoding="utf-8")
        logo = ''

        if TG == "True":
            logo = logo + '<img align="right" id="ms_logo" src="ico/Telegram.png">'
        if DS == "True":
            logo = logo + '<img align="right" id="ms_logo" src="ico/discord-512.webp">'


        try:
            file.write(B[0] + '<cut><a href="'+URL+'"><div class="Bot"' + 'id="' + id +'"><img align="left" id="ava" src="' + Ava+ '"></a><h1>' + Name + '</h1><p>' + Description + '</p>'+logo+'</div><cut>' + B[2])
        except:
            pass

    class Creat:
        def Creat_Bone():
            pass

class Config:

    def Get(file_name="D:\BotHub 1.2\main_cfg.sws", name="None", finde="Token"):
        obj = CuteON.Get_.getObj(file=file_name, nameObj=name)
        return CuteON.Get_.getLineText(obj, finde)
        


