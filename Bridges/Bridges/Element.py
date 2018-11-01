#!/usr/bin/env python
from Bridges.ElementVisualizer import *
from Bridges.Color import *
from Bridges.LinkVisualizer import *
import re

 ## \mainpage BRIDGES
 #
 # \section overview_sec Overview
 #  The Bridging Real-world Infrastructure Designed to Goal-align, Engage, and
 #  Stimulate (BRIDGES) project is directed at improving the retention of sophomore
 #  students in Computer Science by (1) introducing real-world datasets (Facebook,
 #  Twitter, etc) into course projects involving computer science data structures,
 #  and (2) facilitating peer mentoring of sophomores by senior CS students in
 #  shared lab experiences that involve the use of the BRIDGES infrastructure in
 #  software development.
 #  \section br_client BRIDGES Client Design
 #  BRIDGES client side design loosely follows the basic data structure elements
 #  implemented and described in ``A Practical Introduction to Data Structures and
 #  Algorithm Analysis" by C.A. Shaffer (http://people.cs.vt.edu/shaffer/Book/).
 #  These elements are augmented to contain visual properties that are controlled
 #  by the user to customize the visual representation of the constructed data structure.
 #  Once a a data structure is ready to be visualized, related BRIDGES server calls are
 #  made to send a reprsentation of the data structure to BRIDGES server.
 #  \section br_server BRIDGES Server Design.
 #  BRIDGES server implements a combination of technologies (MongoDB, Node,
 #  d3JS(visualization) to receive a data structure representation for visualization.
 #  These are largely transparent to the user and involves the user being directed to a
 #  web page for viewing the data structure. Attention has been paid to provide
 #  meaningful error messages to the user in case problems are encountered in the process.
 #  \section api_sec API Descriptions.
 #  See the accompanying pages for detailed description of the BRIDGES classes
 #  \subsection sponsor_sec Sponsorship/Funding.
 #  BRIDGES is an NSF TUES Project.
 #
 #  \section contacts_sec Contacts:
 #  Kalpathi Subramanian, krs@uncc.edu, Jamie Payton, payton@temple.edu,
 #  Erik Saule, esaule@uncc.edu
 #
 #  Department of Computer Science, The University of North Carolina at Charlotte,
 #  Charlotte, NC.
 ##


##
# @brief This is the main superclass in BRIDGES for  deriving a number of
# 	objects used  in building arrays, lists, trees and graph data structures.
#  SLelement, DLelement, CircSLelement, CircDLelement, TreeElement, BinTreeElement,
#	BSTElement, CircSLelement, CircDLelement, AVLTreeElement are all subclasses
#  (see class hierarchy above).  Element contains  two
#	visualizer objects (ElementVisualizer, LinkVisualizer) for specifying
#	visual attributes for nodes and links respectively. It also contains a label that
#	that can be displayed in BRIDGES visualizations.
#
#  All the tutorials under
#
#	http://bridgesuncc.github.io/Hello_World_Tutorials/Overview.html
#
#  illustrate examples of using different types of Element objects and how to
#	manipulate their visual attributes.
#
# @author Mihai Mehedint, Kalpathi Subramanian
#
#
class Element(object):

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    ids = 0
    label = str()
    identifier = str()
    # visualizer = ElementVisualizer()
    # print(visualizer)
    # lvisualizer = dict()
    value = object()

    #
    # 	this is the number of pattern matches where the new string
    #  	can be inserted; useful in case we insert line breaks at a
    #  	desired number of characters is the pattern is change to
    # 	white space this index can be changed to 2 words to insert a
    # 	line break every 2 words
    word_number = 0

    # this is the string value that replaces the pattern found in the label
    INSERT_STRING = "\\n"

    # 	for more complex patterns the key must be changed
    # 	like so "((John) (.+?))" returns "John firstWordAfterJohn":
    # 	John writes, John doe, John eats etc.
    # 	(\\w) matches any word (\\d) any digit (\\D) any non digit
    # 	(\\s) a white space (\\s*) zero or more whitespaces, (\\s+)
    # 	one or more
    DIVIDE_KEY = "(\r?\n)|(\n)|(\f)|(\r)|(%n)"

    # public String INSERT_STRING = "\\n";
    # public String DIVIDE_KEY ="(\n)";
    def get_data_struct_type(self):
        return "Element"

    ##
    # Element constructor
    # creates an ElementVisualizer object
    # sets a unique identifier for the current Element
    # normally used from subclasses
    # @param val generic parameter value used to construct Element
    # @param label the string that is visible on the Bridges Visualization
    #
    def __init__(self, label = None, val=None, original=None):
        Element.ids += 1
        self.visualizer = ElementVisualizer()
        self.lvisualizer = dict()
        # super(Element.Element, self).__init__()
        if val is not None and label is None and original is None:
            self.set_value(val)
            self.identifier = str(Element.ids)
            self.label = "Default"
            self.set_visualizer(ElementVisualizer())
            self.ids = Element.ids
            self.lvisualizer = dict()
        if val is not None and label is not None:
            self.identifier = str(Element.ids)
            self.label = "Default"
            self.set_visualizer(ElementVisualizer())
            self.ids = Element.ids
            self.lvisualizer = dict()
            self.set_label(label)
            self.set_value(val)
        if original is not None:
            self.identifier = str(Element.ids)
            self.ids = Element.ids
            self.label = str(original.get_label())
            self.visualizer = ElementVisualizer(original.get_visualizer())
            self.lvisualizer = dict()
            self.set_value(original.get_value())
        if val is None and label is None and original is None:
            self.identifier = str(Element.ids)
            self.label = "Default"
            self.set_visualizer(ElementVisualizer())
            self.ids = Element.ids
            self.lvisualizer = dict()
            # print(str(self.__dict__))

    ##
    # this method returns the element's unique identifier
    # @return the string identifier
    #
    def get_identifier(self):
        return self.identifier

    ##
    # Returns the Element's visualizer object
    #
    # @return the visualizer object
    #
    def get_visualizer(self):
        return self.visualizer

    ##
    # This method sets the visualizer object for the current
    # element object
    #
    # @param visualizer the visualizer to set
    #
    def set_visualizer(self, visualizer):
        self.visualizer = visualizer

    ##
    # Returns the Element's link visualizer object
    #
    # The link visualizer object links this element to another element, which
    # is specified by the argument to this method. This method is typically used
    # to set the visual attributes of the links, such as in graphs or binary tree
    # structures.
    #
    # @parm Element el -- the element terminating the link
    #
    # @return the link visualizer
    #
    def get_link_visualizer(self, el):
        #  if this is the first time, must create the
        #  link visualizer
        if el in self.lvisualizer:
            return self.lvisualizer[el]
        else:
            self.lvisualizer[el] = LinkVisualizer()
            return self.lvisualizer[el]

    ##
    #	Sets the link from this element to a new incoming element
    #
    #	@param el the element to be linked to.
    #
    #
    def set_link_visualizer(self, el):
        self.lvisualizer[el] = LinkVisualizer()

    def remove_link_visualizer(self, el):
        self.lvisualizer.pop(el)

    ##
    # Validates the Element's value when the Element is created
    # A non null value is expected
    # this will be unnecessary after we modify the server
    # @param Element value
    #
    # def validate_val(self, value):
    #     try:
    #         if value == None:
    #             raise NullPointerException("\nInvalid value set to Element<E> '" + value + "'. Expected" + " non null E value.\n")
    #         elif value.__class__.getCanonicalName().isEmpty():
    #             raise IllegalArgumentException("\nThe argument is not a legal Element object!\n" + value.__class__.getCanonicalName())
    #         else:
    #     except Exception as e:
    #         e.print_stack_trace()
    def get_class_name(self):
        return self.value.__class__.__name__

    # def compare_to(self, e1):
    #     if e1 == None:
    #         raise NullPointerException("The object you are comparing to is null.")
    #     return self.get_label().compareTo(e1.getLabel())

    # def equals(self, e1):
    #     if e1 == None:
    #         raise NullPointerException("The object you are comparing to is null.")
    #     return self.get_label() == e1.getLabel() and self.get_identifier() == e1.get_identifier() and self.get_value() == e1.get_value() and self.getVisualizer() == e1.getVisualizer()

    def get_element_representation(self):
        json_str = self.OPEN_CURLY + self.QUOTE + "name" + self.QUOTE + self.COLON + self.QUOTE + str(self.label) + self.QUOTE + self.COMMA + self.QUOTE + "shape" + self.QUOTE + self.COLON + self.QUOTE + self.visualizer.get_shape() + self.QUOTE + self.COMMA + self.QUOTE + "size" + self.QUOTE + self.COLON + str(self.visualizer.get_size()) + self.COMMA + self.QUOTE + "color" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.visualizer.get_color().get_red()) + self.COMMA + str(self.visualizer.get_color().get_green()) + self.COMMA + str(self.visualizer.get_color().get_blue()) + self.COMMA + str(self.visualizer.get_color().get_alpha()) + self.CLOSE_BOX
        # loc_flag = not ((self.visualizer.getLocationX() == Double.POSITIVE_INFINITY) or (self.visualizer.getLocationY() == Double.POSITIVE_INFINITY))
        # if loc_flag:
        #     json_str += self.COMMA + self.QUOTE + "location" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.visualizer.get_locationX()) + self.COMMA + str(self.visualizer.get_locationY()) + self.CLOSE_BOX
        # if self.get_data_struct_type() == "BinarySearchTree":
        #     bst = BSTElement(self)
        #     json_str += self.COMMA + self.QUOTE + "key" + self.QUOTE + self.COLON + self.QUOTE + bst.getKey().__str__() + self.QUOTE + self.COMMA
        # elif self.get_data_struct_type() == "AVLTree":
        #     json_str += self.COMMA + self.QUOTE + "key" + self.QUOTE + self.COLON + self.QUOTE + avl.getKey().__str__() + self.QUOTE + self.COMMA + self.QUOTE + "height" + self.QUOTE + self.COLON + Integer.toString(avl.getHeight()) + self.COMMA + self.QUOTE + "balance_factor" + QUOTE + COLON + Integer.toString(avl.getBalanceFactor()) + COMMA
        # else:
        json_str += self.CLOSE_CURLY
        return json_str

    def get_link_representation(self, lv, src, dest):
        return self.OPEN_CURLY + lv.get_link_properties() + self.COMMA + self.QUOTE + "source" + self.QUOTE + self.COLON + src + self.COMMA + self.QUOTE + "target" + self.QUOTE + self.COLON + dest + self.CLOSE_CURLY

    ##
	#  This method returns the existing value of the label fields
	#
	#  @return the label of the Element; the label is typically displayed on BRIDGES
	#  			visualizations.
	#
    def get_label(self):
        return self.label

    ##
	#  This method sets the label
	#
	#  @param label the label to set
	#
    def set_label(self, label):
        self.label = self.arrange_label(label, self.word_number)

    ##
	#  This method formats the label string using a predefine pattern (DIVIDE_KEY) and
	#  replaces the pattern with the string characters hold by the INSERT_STRING global
	#  variable
	#
	#  @param label  the input label string
	#
	#  @param wordNumber in very long strings in the case where the whitespace
	#  \\s is chosen as a key the wordNumber can be set
	#  to replace the whitespace with a newline character \\n at a given number of
	#  words (every second or third word)
	#  The default value is 0. In most situations we want to replace all patterns found.
	#  for more complex patterns the key must be changed like so "((John) (.+?))"
	#  returns "John firstWordAfterJohn": John writes, John doe, John eats etc.
	#  (\\w) matches any word (\\s) one white space (\\s*) zero or more white spaces,
	#  (\\s+) one or more
	#
	#  @return  the formatted label
	#
    def arrange_label(self, label, word_number):
        my_pattern = re.compile(self.DIVIDE_KEY)
        # match = my_pattern.findall(str(label))
        # if not len(match) == 0:
        return label
        # else:
        #     print ("error")
        #     return str()
            # match.reset()
            # while match.find():
            #     counter += 1
            #     if counter == wordNumber:
            #         counter = -1
            #         match.appendReplacement(str, Matcher.quoteReplacement(self.INSERT_STRING))
            # match.appendTail(str)
            # if len(str) == 0:
            #     return label
            # else:
            #     return label = str.__str__()

    ##
	#  This method returns the generic parameter value held in the element.
	#
	#  @return the value
	#
    def get_value(self):
        return self.value

    ##
	#  This method sets the generic parameter value for  this element.
	#
	#  @param value the value to set
	#
    def set_value(self, value):
        # self.validateVal(value)
        self.value = value

    def __str__(self):
        return "Element [name=" + self.label + ", identifier=" + self.identifier + ", visualizer=" + str(self.visualizer) + ", value=" + self.value + ", getIdentifier()=" + self.get_identifier() + ", getVisualizer()=" + str(self.get_visualizer()) + ", getClassName()=" + self.get_class_name() + ", getElementRepresentation()=" + self.get_element_representation() + ", getLabel()=" + self.get_label() + ", getValue()=" + self.get_value() + ", getClass()=" + self.get_class_name() + ", hashCode()=" + self.hash_code() + ", toString()=" + super(Element, self).__str__() + "]"
