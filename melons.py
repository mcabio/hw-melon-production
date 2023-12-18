"""Melon and Squash classes."""

import robots


class Melon:
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


class Squash(Melon): # Created this new class to accommodate for Squash. It is a subclass of the parent class Melon
    """Winter squash."""

    def __init__(self, melon_type): # This code is inheriting from the parent class Melon, which means that
                                    # it has the same items: melon_type, weight, color, and sticker.
        super().__init__(melon_type) # In lieu of re-writing the same method, super() is used. It is a 
                                     # built-in function that is used to call a method from the parent class. 
                                     # It returns a temporary object of the superclass, which allows you to 
                                     # call its methods

    def prep(self):
        super().prep() # This code is also inheriting the method 'prep' from the Melon class. 
                       # The prep method in the parent class does not take any additional parameters 
                       # beyond self. Therefore, the correct syntax for calling the parent class's 
                       # prep method would be to keep the paranthesis empty in prep().
                       # If super().prep(self) is written, the line is attempting to call the prep 
                       # method of the parent class and passing self as an argument. 
                       # If the parent class's prep method is defined as def prep(self):, 
                       # it does not accept any additional parameters beyond self. 
                       # Therefore, attempting to pass self as an argument would be unnecessary and 
                       # might lead to a TypeError or a similar error.
        robots.painterbot.paint(self) # Since squashes are the only items that need to be painted, 
                                      # this is an attribute unique to squash, so it passes self as a parameter.

    def __str__(self): # This inherits from the __str__ method of the parent class. It's exactly the same
        return super().__str__() + " (squash)" # But, needs a return statement before the super(). Without 
                                               # the return statement, the __str__ method in the child class  
                                               # does not return any value. The super().__str__() calls 
                                               # the __str__ method of the parent class, but it doesn't 
                                               # return or use the result. To fix this, you should include 
                                               # a return statement in the child class's __str__ method, 
                                               # and you might want to append or modify the result obtained 
                                               # from the parent class.
