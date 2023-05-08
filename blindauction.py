print("welcome to the blind auction program")
next = True
auction ={}
auction_list =[]
record_no =0
    
    
while next :
    name= input("what is your name : ")
    bid_amount = int(input("what's your bid : "))
    auction["name"] = name
    auction["bid_amount"] = bid_amount
    auction["record"] =record_no
    auction_list = auction
    print(auction)
    print(auction_list)
    bidder =input("are there any other bidders ? type yes=y or no=n : ").lower()

    if bidder == "n":
        next = False
    elif bidder == "y" :
        record_no = record_no+1
        auction["name"] = name
        auction["bid_amount"] = bid_amount
        auction["record"] =record_no
        auction_list.append(auction)
        print(auction)
        print(auction_list)

