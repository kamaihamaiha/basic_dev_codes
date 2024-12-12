unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	cur_user = unconfirmed_users.pop()
	print("Verifying user: " + cur_user.title())
	confirmed_users.append(cur_user)
	
print("\nThe followding user have been confirmed:")
for user in confirmed_users:
	print(user.title())	