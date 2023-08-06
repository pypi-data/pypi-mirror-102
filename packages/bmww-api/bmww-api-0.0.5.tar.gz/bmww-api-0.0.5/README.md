# bmww-api

Use : pip install bmww-api==0.0.3

to install this module

Pypi url : https://pypi.org/project/bmww-api/

Disclaimers:

- This is not an official api and it is quite weak but it gets the job done.

- DO NOT ABUSE REQUESTS SINCE IT CAN BE HARMFUL FOR THE WEB PAGE.


Notes:


- As said before this is not an official api and it was made by one person, so if you see any errors in the code or see a better way to do code it and know how to do it, you are welcome to edit it.


- Information like genres or information that can be a list (ex: genres, categories, challenges, series) can't be accessed individually due to the way that the html was written. Again if you find a way to fix it or make it possible to access this information individually you are welcome to do it


- If you want to access information like the ones stated above you would have to do .complete_info this will get the work's complete info


- I may be updating this project with new features, however i don't really have much time to do it and since this is one of my first times using beautiful soup the code maybe a bit messy and with a lot of errors.


Quick guide on how to use:

```
#import module
from bmwwAPI import bmww

#create api object
api = bmww()


# create work from api '487' being the id of the work/fanfiction
# https://batmanwonderwoman.com/fanfiction/viewstory.php?sid=487 the last 3 numbers of the url are the id of the work, those are the three numbers you need
# if an id is not given the only information available is to get a random story

# create a work object based on the api
work = api.work(#id)

# some of the functions of the api

# get information out of a work/fanfic/series

work_info = [

  work.title,           # title
  work.author,          # author
  work.reviews,         # reviews
  work.chapters,        # chapters
  work.completed,       # if its completed
  work.words,           # how many words
  work.read,            # times read
  work.published,       # publish date
  work.updated,         # last time updated
  work.url,             # its url
  work.summary,         # its summary
  work.complete_info    # the entire work's info

]


# get information out of an users profile, this gets the information that the user chose to share, so no funny business here.
# you don't have to specify any work's id except the users id

# create an user object based on the api
user = api.users()

# some of the information that you can get from user's profiles

# keep in mind that some of this information may not be available if the user chose not to share it

user_info = [

  user.penname,              # gets the user nickname
  user.real_name,            # gets the user real name   
  user.member_status,        # gets the user member status
  user.bio,                  # gets the user bio
  user.user_url,             # gets the user page url
  user.beta_reader           # gets if the user is a beta reader
  user.gender                # gets the user gender
  user.recent_story          # gets the user's last published or updated story
  user.stories               # gets the number of user published stories
  user.series                # gets the number of user series
  user.reviews               # gets the number of the user reviews
  user.challenges            # gets the number of the user challenges
  user.favorite_series       # gets the number of the user favorite series
  user.user_favorites        # gets the number of user favorites

]

```

For more information in how to use the api, refer to ```example_code.py```
