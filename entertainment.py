import fresh_tomatoes
import media

avatar = media.Movie("Avatar",
                    "A marine set to the moon on a unique mission becomes torn between following his orders and protecting his new world.", "http://img.csfd.cz/files/images/user/profile/159/129/159129345_9e5fe4.jpg",
                      "https://www.youtube.com/watch?v=uZNHIU3uHT4")

interstellar = media.Movie("Interstellar",
                    "A important mission in human history; traveling to the galaxy to discover if mankind has a future among the stars.",  "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=8EdxTFS3fD0")

gravity = media.Movie("Gravity",
                    "A heart-pounding thriller that pulls you into the infinite and unforgiving realm of deep space.",
                    "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                     "https://www.youtube.com/watch?v=YiMMfI0hcGw")

ex_machina = media.Movie("EX MACHINA",
                    "Upon his arrival, Caleb learns that Nathan has chosen him to be the human component in a Turing Test-charging him with evaluating the capabilities.",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                     "https://www.youtube.com/watch?v=3hAlv0xLJJ4")

inception = media.Movie("Inception",
                    "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_(2010)_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=d3A3-zSOBT4")

dont_breathe = media.Movie("Don't Breathe",
                    "A trio of reckless thieves breaks into the house of a wealthy blind man, thinking they'll get away with the perfect heist. They're wrong.",
                     "https://upload.wikimedia.org/wikipedia/en/4/41/Don%27t_Breathe_%282016_film%29.png", "https://www.youtube.com/watch?v=aJToojbRtww")

movies = [avatar, interstellar, gravity, ex_machina, inception, dont_breathe]
fresh_tomatoes.open_movies_page(movies)

