print("welcome to the blind auction program")
next = True
auction ={}
auction_list =[]
record_no =0
bid_counter = 0
    
while next :
   
    bidder =input("are there any other bidders ? type yes=y or no=n : ").lower()
    

    if bidder == "n":
        bio_counter = 0
        next = False
    elif bidder == "y" :
        bio_counter = 1
        name= input("what is your name : ")
        bid_amount = int(input("what's your bid : "))
        auction_len = len(auction_list) +1
        print(auction_len)
        
        #auction_list[auction_len]["name"] = name
        #auction_list[auction_len]["bid_amount"] = bid_amount

        auction_list[0]["name"] = name
        auction_list[0]["bid_amount"] = bid_amount

        print(auction_list)
        auction_len = auction_len + 1

print(auction_list)

       

