initial=1
while initial:
    while True: 
        try:
            status=input('------1 for start  2 for stop--------------: ')
            status=int(status)
        except:
            pass        
        
    
     
        if type(status) is not int:
            break
        else:
            
            if type(status) is  int:
                status=int(status)

                if type(status) is int:
                    gear_status=0
                    while status==1:
                        print("----------------------------engine runing-----------------------------: ")
                    
                        cluth=input(' press cluth for c press s for stop   :')
                        
                        while cluth=='c':
                            print(f'    {gear_status}')
                            gear=input('only 8 for gear up 2 for gear down :')
                            
                            if type(gear) is str:
                                gear=int(gear)
                                if gear==8:
                                    if gear_status <5:
                                        gear_status+=1
                                        print(f'    {gear_status}')
                                    break

                                elif gear==2:
                                    if gear_status>0:
                                        gear_status-=1
                                        print(f'    {gear_status}')
                                    break
                            
                                else:
                                    pass
                            else:
                                pass
                            
                                
                        if cluth=='s':
                            initial=0
                            break
                            
                        else:
                            pass
                    while status==2 or initial==0:
                        print("engine stoped")
                        initial=0
                        break
                    
                    else:
                        pass
                else:
                    pass
            else:
                pass
    


