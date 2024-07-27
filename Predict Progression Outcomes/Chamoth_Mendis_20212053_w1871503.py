# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 

#Student ID - 20212053
#Name - Chamoth Mendis



#Import Student version as a module
while True:
    import Student_version
    print("\n")
    print("User versions")
    print("1.student")
    print("2.staff")
    print("\n")
    option = input("Select your version by entering 1 0r 2 :")

    if option == "1":
        Student_version.myFunction()
        print("\n")
        continue


    if option == "2":
        #Declare Variables
        limit = range(0,121,20)
        Progress = 0
        Trailer = 0
        Retriever = 0
        Excluded = 0
        Total = 0
        progressList = []
        trailerList= []
        retrieverList= []
        excludeList = []

        #defining fuctions to store user inputs using lists.
        def ProgressResult():
            progressSub = []
            progressSub.append(passMark)
            progressSub.append(deferMark)
            progressSub.append(failMark)
            progressList.append(progressSub)


        def moduleTrailerResult():
            trailerSub = []
            trailerSub.append(passMark)
            trailerSub.append(deferMark)
            trailerSub.append(failMark)
            trailerList.append(trailerSub)


        def moduleRetriever():
            retrieverSub = []
            retrieverSub.append(passMark)
            retrieverSub.append(deferMark)
            retrieverSub.append(failMark)
            retrieverList.append(retrieverSub)


        def excludeResult():
            excludeSub = []
            excludeSub.append(passMark)
            excludeSub.append(deferMark)
            excludeSub.append(failMark)
            excludeList.append(excludeSub)
    
    
    
    
        #-------------------------------------------------------------------------------------------------------
        #PART 1
        #Get the user inputs and,Outputs appropriate progression.
        #Inputs = pass,defer,fail Marks
        #outputs = Progress,Progress (module trailer),Do not Progress – module retriever,Exclude.

        while True:
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
                                Progress += 1
                                Total += 1
                                ProgressResult()
                        
                        
                            elif passMark == 100:
                                print("Progress (module trailer)")
                                Trailer += 1
                                Total += 1
                                moduleTrailerResult()

                            
                            elif failMark <= 60 and failMark >= 0 :
                                print("Do not Progress – module retriever")
                                Retriever += 1
                                Total += 1
                                moduleRetriever()


                            
                            elif failMark <= 120 and failMark >= 80:
                                print("Exclude")
                                Excluded += 1
                                Total += 1
                                excludeResult()


               
                            



        #---------------------------------------------------------------------------------------------------------
        #asks from user whether he wants to continue or not
        #To continue he has to input "y"
        #To exit he has to input "q"



                            print("\n")

                    
                    
                            print("Would you like to enter another set of data?")
                    
                            dicesion = input("Enter 'y' for yes or 'q' to quit and view results: ")
                            print("\n")
                            if dicesion == "y":
                                continue
                            if dicesion == "q":


                                #if user wants to exit, the programme will ask outputs option
                                print("How do you want to get outputs ?")
                                optionOne = print("1.Horizontal histogram")
                                optiontwo = print("2.Vertical histogram")
                                optionThree = print("3.User inputs")
                                print("\n")
                                option = input("Select a option from 1,2 and 3 :")


                                #Horizontal histogram

                                if option == "1":
                                    print("Horizontal histogram")
                                    print("Progress ",Progress ,":" ,"*"*Progress)
                                    print("Trailer ",Trailer ,":" , "*"*Trailer)
                                    print("Retriever ",Retriever ,":" , "*"*Retriever)
                                    print("Excluded ",Excluded ,":" , "*"*Excluded)
                                    print("\n")
                                    print(Total," outcomes in total")

                                    print("\n")

                       

        #----------------------------------------------------------------------------------------------------------------
        #PART 2
        #According to the user inputs,display verticle histogram as a output


                                #Verticle histogram accaording to the user inputs        
                                elif option == "2":
                                    category = ["Progress ","Trailer ","Retriever ","Excluded "]
                                    print(" ".join(category))
                                    for i in range(max(Progress ,Trailer ,Retriever ,Excluded)):
                                        print("    {0}        {1}        {2}        {3}".format(
                                        "*" if i < Progress  else "  ",
                                        "*" if i < Trailer   else "  ",
                                        "*" if i < Retriever else "  ",
                                        "*" if i < Excluded  else "  ",
                                        ))

                        

 
        #-----------------------------------------------------------------------------------------------------------------------                        
        #PART 3 ;
        #DISPLAY user inputs as a result
        #PART 3 references from stackoeverflow


        #PART 4;
        #Save input data to a file

                        
                                elif option == "3":
                                    #write inputs to a file
                                    file = open('Outputs.txt','w')
                                    for i in range(len(progressList)):
                                        progressValues = ','.join(str(e) for e in progressList[i])
                                        print("Progress - ",progressValues )

                                        #write inputs to a file
                                        file.write('Progress -')
                                        file.write(progressValues)
                                        file.write('\n')

                                
                                    for i in range(len(trailerList)):
                                        trailerValues = ','.join(str(e) for e in trailerList[i])
                                        print("Progress (module trailer)- ", trailerValues)

                                        file.write('Progress (module trailer) -')
                                        file.write(trailerValues)
                                        file.write('\n')
                                    


                                    for i in range(len(retrieverList)):
                                        retrieverValues = ','.join(str(e) for e in retrieverList[i])
                                        print("Module retriever - ", retrieverValues)

                                        file.write('Module retriever -')
                                        file.write(retrieverValues)
                                        file.write('\n')


                                    for i in range(len(excludeList)):
                                        excludeValues = ','.join(str(e) for e in excludeList[i])
                                        print("Exclude -", excludeValues)

                                        file.write('Exclude -')
                                        file.write(excludeValues)
                                        file.write('\n')
                                    file.close()
                                    print("\n")


                                    #read from the file
                                    print("Reading from the file ;")
                                    print("\n")
                                    file = open("Outputs.txt",'r')
                                    print(file.read())
                                    


                                break
                            
                        
                        


                        else:
                            print("Out of range")
                
                    else:
                        print("Out of range")
            
                else:
                    print("Out of range")


            except ValueError:
                print("Integer required")

        
            
            

