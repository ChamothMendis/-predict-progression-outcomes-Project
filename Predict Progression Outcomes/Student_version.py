def myFunction ():
    limit = range(0,121,20)
    try:
        passMark = int(input("Please enter your credits at pass :"))
        if passMark in limit:
            deferMark = int(input("Please enter your credits at defer :"))
            if deferMark in limit:
                failMark = int(input("Please enter your credits at fail :"))
                if failMark in limit:
                    total = passMark + deferMark + failMark
                    if total != 120:
                        print("Total incorrect")

                    elif passMark == 120:
                        print("Progress")
                        
                        
                        
                    elif passMark == 100:
                        print("Progress (module trailer)")
                        
                        

                            
                    elif failMark <= 60 and failMark >= 0 :
                        print("Do not Progress – module retriever")
                        
                            
                    elif failMark <= 120 and failMark >= 80:
                        print("Exclude")
                        

                else:
                    print("Out of range")
                
            else:
                print("Out of range")
            
        else:
            print("Out of range")


    except ValueError:
        print("Integer required")

                            
