import unittest
import Main_MovieRatingSystem

class test_Main_MovieRatingSystem(unittest.TestCase):
    def test_display_menu(self):
        actual = Main_MovieRatingSystem.display_menu("1. Add a Movie \n 2. Rate a Movie \n  3. View Average Ratings \n  4. Exit")
        expected = "1. Add a Movie \n 2. Rate a Movie \n  3. View Average Ratings \n  4. Exit"
        self.assertEqual(actual, expected)
        
    def test_that_user_choice_is_in_the_range_of_one_to_four(self):
        self.assertTrue(Main_MovieRatingSystem.validate_user_choice(1))
        self.assertTrue(Main_MovieRatingSystem.validate_user_choice(2))
        self.assertTrue(Main_MovieRatingSystem.validate_user_choice(3))
        self.assertTrue(Main_MovieRatingSystem.validate_user_choice(4))
        
    def test_that_user_choice_does_not_accept_number_below_or_higher_the_range_of_one_to_four(self):
        self.assertFalse(Main_MovieRatingSystem.validate_user_choice(0))
        self.assertFalse(Main_MovieRatingSystem.validate_user_choice(-1))
        self.assertFalse(Main_MovieRatingSystem.validate_user_choice(50))
        
    def test_that_movie_name_is_not_empty(self):
        self.assertTrue(Main_MovieRatingSystem.add_movie("336 days of war"))
        self.assertTrue(Main_MovieRatingSystem.add_movie("336 Days of WAR"))
        self.assertTrue(Main_MovieRatingSystem.add_movie("336 DAYS OF WAR"))
    def test_that_movie_name_return_false_if_movie_name_is_empty(self):
        self.assertFalse(Main_MovieRatingSystem.add_movie(" "))
        
    def test_that_movie_name_to_rate_is_thesame_as_movie_in_add_movie(self):
        self.assertTrue(Main_MovieRatingSystem.validate_movie_name_to_rate("336 days of war"))
        self.assertTrue(Main_MovieRatingSystem.add_movie("336 Days of WAR"))
        self.assertTrue(Main_MovieRatingSystem.add_movie("336 DAYS OF WAR"))
        
    def test_that_movie_name_to_rate_return_false_if_movie_name_to_rate_is_not_thesame(self):
        #self.assertFalse(Main_MovieRatingSystem.validate_movie_name_to_rate("336 days of war", "play game day"))
        self.assertFalse(Main_MovieRatingSystem.validate_movie_name_to_rate(" "))
    
    
    def test_that_rating_number_is_in_the_range_of_one_to_five(self):
        self.assertTrue(Main_MovieRatingSystem.validate_rating_range(1))
        self.assertTrue(Main_MovieRatingSystem.validate_rating_range(2))
        self.assertTrue(Main_MovieRatingSystem.validate_rating_range(3))
        self.assertTrue(Main_MovieRatingSystem.validate_rating_range(4))
        self.assertTrue(Main_MovieRatingSystem.validate_rating_range(5))
        
    def test_that_rating_number_is_not_less_than_the_range_of_one_to_five(self):
        self.assertFalse(Main_MovieRatingSystem.validate_rating_range(-1))
        self.assertFalse(Main_MovieRatingSystem.validate_rating_range(0))
        self.assertFalse(Main_MovieRatingSystem.validate_rating_range(-999))
        
    def test_that_rating_number_is_not_greater_than_the_range_of_one_to_five(self):
        self.assertFalse(Main_MovieRatingSystem.validate_rating_range(9))
        self.assertFalse(Main_MovieRatingSystem.validate_rating_range(99))
        