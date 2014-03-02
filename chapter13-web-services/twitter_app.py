import importlib

# these should be encrypted
TWITTER_CONSUMER_KEY = 'DeH9TfrfeV7UeRgK3OSGA'
TWITTER_CONSUMER_SECRET = 'sZGBB28VZcrRfcZvexYydj2Pc2uWW307kP8l7T7yiQo'
TWITTER_OAUTH_TOKEN = '2334856880-zYwvSu8kS7cGfH67lQ64vulTUbY7zxhc39bpnlG'
TWITTER_OAUTH_TOKEN_SECRET = 'RTQ7pzSytCIPsASCkA0Z5rubpHSWbvjvYR3c3hb9QhC3M'


CMDs = {
    'twython': {
        # key = Twitter API name
        # value = Twython method name (when null Twitter API name = Twython method name)
        'search':               None,
        'verify_credentials':   None,
        'user_timeline':        'get_user_timeline', # this function is named differently in Twython
        'update_status':        None,
        'module': None
    },
    # tweepy is not installed just kept for the example
    'tweepy': dict.fromkeys((
        'search',
        'verify_credentials',
        'user_timeline',
        'update_status',
        'module'
    )),
}
APIs = set(CMDs)

# remove unavailable APIs
remove = set()
for api in APIs:
    try:
        # __import__(api) # this also works but is meant for use by the Python interpreter
        CMDs[api]['module'] = importlib.import_module(api) # store the imported package
    except ImportError:
        remove.add(api)
        # can also be done with -> APIs.remove(api)
        # but it's a good example for -> difference_update

APIs.difference_update(remove) # removes from set "APIs" the values in the set "remove"
if not APIs:
    raise NotImplementedError(
        'No Twitter API found; install one & add to CMDs!')
# at this point APIs has only the names of the modules that exists

# this is a wrapper for calling the real twitter API
class Twitter():
    def __init__(self, api):
        self.api = api
        if api == 'twython':
            self.twitter = CMDs[api]['module'].Twython(
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET,
                TWITTER_OAUTH_TOKEN,
                TWITTER_OAUTH_TOKEN_SECRET)
        elif api == 'tweepy':
            auth = CMDs[api]['module'].OAuthHandler(TWITTER_CONSUMER_KEY, consumer_secret)
            auth.set_access_token(TWITTER_OAUTH_TOKEN, TWITTER_OAUTH_TOKEN_SECRET)
            self.twitter = CMDs[api]['module'].API(auth)

    def _get_method(self, cmd):
        method_name = CMDs[self.api][cmd] # the value
        if not method_name:
            # if value = None
            method_name = cmd # the key (it means Twitter API name = Twython method name)
        return getattr(self.twitter, method_name)

    def search(self, str_to_search):
        if self.api == 'twython':
            results = self._get_method('search')(count=3, q=str_to_search)['statuses']
            data = ((tweet['user']['screen_name'], tweet['created_at'], tweet['text']) for tweet in results)
            return list(data)
        elif self.api == 'tweepy':
            return (ResultsWrapper(tweet)
                for tweet in self._get_method('search')(q=str_to_search))
        else:
            return None

    def verify_credentials(self):
        f = self._get_method('verify_credentials')
        return ResultWrapper(f())
        
    def user_timeline(self):
        f = self._get_method('user_timeline')
        # return ResultWrapper(f())
        return f()

    def update_status(self, tweet):
        f = self._get_method('update_status')
        return ResultWrapper(f(status=tweet.encode('utf-8'))) # encode for Python v3.x

class ResultWrapper():
    # if we do not know if obj is a class or a dictionary
    # then with this class we can use it always as a class

    # if obj is a class then the call foo.bar works
    # if obj is a dictionary then the foo.bar also works even if foo['bar'] is the correct
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return repr(self.obj)

    def __getattr__(self, attr):
        if hasattr(self.obj, attr):
            return getattr(self.obj, attr)
        elif hasattr(self.obj, '__contains__') and attr in self.obj:
            return self.obj[attr]
        else:
            raise AttributeError(
                '%r has no attribute %r' % (self.obj, attr))

    __getitem__ = __getattr__

        
if __name__ == '__main__':
    for api in APIs:
      twitter = Twitter(api)
      print('*** %s ***' % api)

      print('SEARCH')
      results = twitter.search('python')
      for item in results:
          print('user: ', item[0])
          print('created at: ', item[1])
          print('test: ', item[2])
          print()
      
      print('VERIFY CREDENTIALS')
      result = twitter.verify_credentials()
      print('user: ', result.screen_name)
      print('created at: ', result.status['created_at'])
      print('status: ', result.status['text'])
      print()

      print('USER TIMELINE')
      results = twitter.user_timeline()
      for item in results:
          print('created at: ', item['created_at'])
          print('status: ', item['text'])
          print()

      print('UPDATE STATUS')
      new_post = 'and yet another tweet using {0}'.format(api)
      result = twitter.update_status(new_post)
      print('created at: ', result.created_at)
      print('current status: ', new_post)
   
      
