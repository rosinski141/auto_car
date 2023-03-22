location = getCurrentLocation()
targetLocation = getCustomerLocation() 
resturantLocation = getResturantLocation()

if(location = targetLocation) :
    sendMessageToCustomer("I have arrived near your location, lookout for" + carDetails()") 

if(location = resturantLocation) :
    sendMessageToResturant("I have arrrived, please prepare the order " + orderNum")
