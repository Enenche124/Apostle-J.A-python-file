import datetime

now = datetime.datetime.now()
current = now.strftime('%Y-%m-%d %H:%M:%S')

def display_menu(menu):
    return "1. Add a Movie \n2. Rate a Movie \n3. View Average Ratings \n4. Exit"

def validate_user_choice(choices):
    if choices < 1 or choices > 4:
        return False
    else:
        return True
def add_movie(movie_name):
    if movie_name.strip():
        return True
    else:
        return False
 
def validate_movie_name_to_rate(movie_name, movies):
    movie_name = movie_name.lower()
    if movie_name in movies:
        return True        
    return False
        
        
def validate_rating_range(rating_range):
    if rating_range < 1 or rating_range > 5:
        return False
    else:
        return True
        
        
        

def main():
    movies = {}
    
   
    while True:
        menu = display_menu("")
        print(menu)
        
        while True:
            try:
                choice = int(input("Enter your choice between 1 - 4: "))
                if validate_user_choice(choice):
                    break
            #else:
                #continue
            except ValueError:
                print("Choice must be between 1 - 4")
               
        if choice == 1:
            
            while True:
                movie_name = input("Enter the movie name: ")
                if add_movie(movie_name):
                    convert_movie_name = movie_name.lower()
                    if movie_name not in movies:
                       movies[convert_movie_name] = {'date': current, 'ratings': []}
                       print(f"Movie {movie_name} added!")
                       break
                    else:
                       print(f"movies {movie_name} already exist.")
                       break
                else:
                    print("Movie name can not be empty.")
                    continue
                  
        elif choice == 2:
            
            while True:
              if not movies:
                print("No movie have been add")
                break
                
              else:
                rating_name = input("Enter the movie name to rate: ")
                convert_rating_name = rating_name.lower()
                if validate_movie_name_to_rate(convert_rating_name, movies):
                    
                    
                    while True:
                       try:
                          rating_value = int(input("Enter rating value: "))
                          if validate_rating_range(rating_value):
                         
                             movies[convert_rating_name]['ratings'].append(rating_value)
                             print(f"Rating added for {rating_name} '{rating_value}")
                             break
                          else:
                            print("invalid, Enter rating between 1 - 5.")
                       except ValueError:
                            print("Invalid, Rating must be an integer between 1 - 5.")
                    break
                else:
                    print("Movie name not found.")
        elif choice == 3:
          if not movies:
            print("No average_rating.")
          else:
            for movie, rate in movies.items():
                if rate['ratings']:   
                    average_rating = sum(rate['ratings']) / len(rate['ratings'])
                    print(f"Average rating for {movie}: {average_rating}")
                else:
                    print(f"{movie} has no rating yet.")  
        elif choice == 4:
            print("Exiting the app, Goodbye🙋‍♂️")
            break            
                              
if __name__ == "__main__":
    main()