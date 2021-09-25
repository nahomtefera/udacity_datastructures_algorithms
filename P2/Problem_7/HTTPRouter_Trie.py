class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, routes, handler):
        node = self.root
        if handler is None:
          handler = self.not_found_handler
        # Keep track of the last item in the route
        # that's where the handler will be
        last_route = routes[len(routes)-1]
        for route in routes:
          if route in node.children:
            node = node.children[route]
            continue
          if route == last_route:
            # Insert the handler in the elast element in the route
            node.insert(route, handler)
          else:
            # Inser not found handler
            # on the paths before the full route
            node.insert(route, self.not_found_handler)
            node = node.children[route]
                
    def find(self, routes):
        node = self.root

        for route in routes:
          if not route in node.children:
            return self.not_found_handler
          node = node.children[route]
        
        return node.handler

class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
    def insert(self, route, handler):
        # Insert the node as before     
        if not route in self.children:
          self.children[route] = RouteTrieNode(handler)
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler="oops, something went wrong :(, blame the marketing dep :|"):
        self.trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler=None):
        if path is None or path == "":
          return "Path can't be null or empty"
        trie = self.trie
        routes = self.split_path(path)
        trie.insert(routes, handler)

    def lookup(self, path):
        if path is None or path == "":
          return "Path can't be null or empty"
        trie = self.trie
        routes = self.split_path(path)
        return trie.find(routes)

    def split_path(self, path):
        routes = path.split('/')
        routes = [route for route in routes if route != ""]

        return routes


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print('lookup /',router.lookup("/")) # should print 'root handler'
print('lookup /home',router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print('lookup /home/about',router.lookup("/home/about")) # should print 'about handler'
print('lookup /home/about/',router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print('lookup /home/about/me',router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


print("\n\nadditional test cases ====> \n ")

## Additional test cases

router_test1 = Router("root handler") # creating a router with no error handler, but we have a safeguard
router_test1.add_handler("/events/", "event handler")
router_test1.add_handler("/news/article", "article handler")

# Adding handler with null path
router_test1.add_handler(None, "null path") # returns "Path can't be null or empty"

# Adding handler with empty handler value
router_test1.add_handler("/news/article/234123412341234134") # add the path with generic error handler 

# Looking up empty path
print('lookup empty path',router_test1.lookup(None)) # returns "Path can't be null or empty"

print('lookup /events/',router_test1.lookup("/events/")) # returns 'event handler'

print('lookup /news/article/234123412341234134',router_test1.lookup("/news/article/234123412341234134")) # returns generic error handler 