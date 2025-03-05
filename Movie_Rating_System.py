movies = {}
average_rating  = 0

while True:

	print("\n 1. Add a Movie \n 2. Rate a Movie \n 3. View Average Rating \n 4. Exit")

	user_choice = int(input("\nEnter your choice: "))

	if user_choice == 1:

		movie_box = input("Enter the movie name: ")
		print(f"movie {movie_box} added!")

	if user_choice == 2:

		title = input("Enter the movie name: ")

		rating = int(input("Enter your rating (1-5): "))

		if title in movies:

			movies[title].append(rating)

		else:
			movies[title] = [rating]

	elif user_choice == 3:

		for title, ratings in movies.items():

			average_rating = sum(ratings) / len(ratings)

			print(f"{title}: {average_rating:.2f}")

		if average_rating  == 0:

			print("No rating yet")

	elif user_choice == 4:

		print("Exiting the application. Goodbye!")

		break