def speed_check(speed):
    if speed<=70:
        return "ok"
    else:
        speed1=(speed-70)/5
        
        if speed1<=12:
            return (f"point:{speed}")
        else:
            return ("license suspended")
enter=speed_check(int(input("enter speed:")))
print(enter)