

         
friendships = [
			   [0,1,1,0,0,0,0,0,0,0]
			   [1,0,1,1,0,0,0,0,0,0]
			   [1,1,0,1,0,0,0,0,0,0]
			   [0,1,1,0,1,0,0,0,0,0]
			   ]


print friendship[0][2] == 1

#True, 0 and 2 are friends


friends_of_five = [i 
                   for i, is_friend in enumerate(friendships[5])
                   if is_friend]

                   
