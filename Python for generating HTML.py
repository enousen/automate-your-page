def generate_concept_HTML(title, paragraph):
    html_text_1 = '''
<div class="concept">
    <div class="title">
        <p>
            <b>
        ''' + title
    html_text_2 = '''
            </b>
        </p>
    </div>
    <div class="paragraph">
        <p>
        ''' + paragraph
    html_text_3 = '''        </p>
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+len('TITLE:')+1 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+len('DESCRIPTION:')+1 :]
    return description

def get_concept_by_number(text, concept_number):
    count = 0
    while count < concept_number:
        count = count + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEXT_LESSON_1 = """TITLE: World Wide Web
DESCRIPTION: The web is a collection of HTML documents connected by hyperlinks. There are about 30 billion pages. Browser requests via the internet to servers use HTTP. Servers respond with files that the browser displays, and servers host the files.
TITLE: HTML
DESCRIPTION: HTML (hypertext markup language) provides the structure. It contains <b>text content</b> (what you see) and <b>markup</b> (what it looks like). You can also enter comments (HTML: !comment; CSS: / * comment * /; Python: #).
TITLE: Tags and Elements
DESCRIPTION: Tags are formatted with the opening tag, "content", closing tag. Both tags and content form an <em>element.</em> If a tag has no end tag, it is a <b>void tag</b>. There are inline, block, and container tags. Elements like h1, h2, etc. contain semantic meaning and style rules.
TITLE: White Space
DESCRIPTION: All spaces (tabs, enters, multiple spaces) are viewed as a single space in HTML. You can use br (break) tag or p (paragraph) tag to add in extra spaces.
TITLE: HTML Documents
DESCRIPTION: HTML documents contain: doctype, HTML tag, head tag (CSS styling goes here), title tag (title of page in top of browser window/tab), body tag (content of document).
TITLE: HTML Documents
DESCRIPTION: HTML documents contain: doctype, HTML tag, head tag (CSS styling goes here), title tag (title of page in top of browser window/tab), body tag (content of document).
"""
TEXT_LESSON_2 = """TITLE: Developer Tools
DESCRIPTION: You can access HTML and CSS of a webpage via the Developer Tools; however, not all elements are in structure (ie header). You can click the element in the tools and see details (font size, border width, color). Conversely, you can also right-click the actual element and then "Inspect Element" and see details in Developer Tools. All elements are <i>rectangular</i>, as boxes make it easier to arrange elements. You use div to define boxes.
TITLE: DOM
DESCRIPTION: Elements are contained via the tree-like/branching structure called <em>Document Object Model (DOM)</em>. This is how the browser organizes tags, elements, content.
TITLE: CSS
DESCRIPTION: CSS provides the style; pages can have identical HTML but look totally different because of CSS. You can give "class" attribute to each element with unique names in order to tell what they are.
"""
TEXT_LESSON_3 = """TITLE: Adding CSS
DESCRIPTION: You need to add certain tags (!DOCTYPE html and html) to tell browser how to interpret code. You add head tag and then either put in style that will apply to the full document or put the link to the file of style code. In this file, you'll define class titles with the style that you want. You can also add style in the HTML file by using the style tag, but this leads to redundancies if it is done inline.
TITLE: DOM
DESCRIPTION: Elements are contained via the tree-like/branching structure called <em>Document Object Model (DOM)</em>. This is how the browser organizes tags, elements, content.
TITLE: Cascading Style Sheets
DESCRIPTION: CSS stands for <u>Cascading Style Sheets</u> and the "cascading" part means that the most specific rule is applied to an element. <b>Inheritance</b> is the idea that properties are applied to the descendants of an element; properties like color, font, etc. are inherited from ancestor elements. <b>This makes it so you don't have to re-declare properties, eliminating redundancies</b>. Using inheritance to apply styles to multiple elements without having to rewrite them allows developers to write less CSS, which speeds up loading of web pages and saves money on development costs.
TITLE: Selectors
DESCRIPTION: <b>Selectors</b> define the elements that styles will apply to. Style rules will apply to all tags that you define; you can use established element types (like h1 or p) to define all of those types of elements or use <b>class selectors</b> to name elements to style them differently based on class names. The <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference">CSS reference list</a> is very helpful in listing and explaining the CSS attributes.
TITLE: The Box Model
DESCRIPTION: The Box Model contains the components of an element: <b>margin</b> (no background color, the space between boxes), <b>border</b> (surrounds padding/content), <b>padding</b> (space in box around content), and <b>content</b> (image, text). You can calculate the size of an element by adding together the pixels of all of these components. If you set the size as a percentage, the element will adjust depending on the screen size. You can also position elements by using { display: flex; }, which will allow divs to appear next to each other.
TITLE: Testing CSS
DESCRIPTION: When making your document, first start with structure. Then move on to defining and using tags, sizing elements, and finally positioning them. Then you can test and refine to make small fixes (font, color, etc). You can test the validity of your <a href="https://jigsaw.w3.org/css-validator/#validate_by_input">CSS</a> and <a href="http://validator.w3.org/#validate_by_input">HTML</a> codes to make sure that it will work for all browsers.
"""
TEXT_LESSON_4 = """TITLE: Computer & Programs
DESCRIPTION: <b>Computers</b> are defined as being universal machines that can do any computation that you can write a program for, and they can execute billions of instructions very quickly. <b>Programs</b> are precise sequence of steps necessary to tell a computer what to do and make it useful. <b>High-level languages</b> like Python avoid the ambiguity and verbosity that a natural language would bring and use interpreters. <b>Input</b> is the code given to an <b>interpreter</b>, which interprets and executes the code.
TITLE: Python
DESCRIPTION: Precise use of spacing and grammar are important in Python. The Backus-Naur form is used for expressions, which uses <i>derivation</i> to replace non-terminals with other non-terminals, a combination of non-terminals, and finally terminals. Arithmetic grammar, for example, uses Expression-Operator-Expression format; as a <i>recursive definition</i>, it needs terminal and non-terminal rules to allow derivation. Also, Python will put an answer in integers if all numbers in the expression are integers.
"""
TEXT_LESSON_5 = """TITLE: Variables
DESCRIPTION: Assigning a name (variable) to an value (expression) makes code readable and meaningful. <b>Assignment statements</b> link the variable name to the value, and they need to start with a letter or an underscore (convention is to use lowercase). You can then use the variable in calculations, and variable values will be updated if calculations change. In this way, you can use the same variable in the assignment statement because <i>the right side of the assignment statement is evaluated first</i>. <br>Example: if days=48, then output of days=days-1 is 47. <b><br><br>"=" does not mean the statement is an equality; it means the assignment of the right side's value to the variable on the left.</b>
TITLE: Strings
DESCRIPTION: Strings are a sequence of characters surrounded by quotes (single or double; must match). "+" can be used to concatenate strings, but you'll need to manually add spaces. You can also multiply strings to repeat the strings. You can't concatenate strings with integer objects.
TITLE: Indexing Strings
DESCRIPTION: Indexing strings is extracting sub-sequences from a string. All extractions use square brackets, and the first character in a string starts at 0. Using negative numbers counts from the end of the string. You can do <b>one character extraction</b> or <b>subsequence extraction</b>. In subsequence extraction, you can select a range or everything up to or after a position. In one character extraction, if there is no character in a certain position, you'll get an error. In contrast, if there are no characters in a subsequence range, you'll get a blank output.
TITLE: Find
DESCRIPTION: <b>Find</b> is a method/procedure that reports the first occurrence of a target string in a search string. If the target string is not in the search string, the output is -1. You can add parameters to say at what position to start the search in order to find later occurrences.
"""
TEXT_LESSON_6 = """TITLE: <b>Functions</b><br>(Procedures)
DESCRIPTION: Use "def" to define your own functions (some, like "find", are built in) and parameters. Make sure to put a colon after the end of the parameters! You can combine functions or use them multiple times in print statement. This powerful tool is called <b>procedure composition</b>. Once you define a function, it can be used forever and thus helps avoid repetition in programming.
TITLE: Input & Output
DESCRIPTION: <b>Input</b> is information that is passed into the parameters of the function. <b>Output</b> is the end result, what is printed after the function is executed (also known as "calling a function"). There needs to be a return statement within a function to see the output. The values of input variables do not change outside of the function, so to see the updated values you need a return statement.
"""
TEXT_LESSON_7 = """TITLE: If and Else
DESCRIPTION: You can use an If Statement for comparison to generate different outcomes. Additionally, if the test expression in the if statement is false, you can use "else" to set up action to take. != means not equal while == means equality (not assignment).
TITLE: Or Operator
DESCRIPTION: Or can be used to evaluate different expressions but things will only be evaluated if needed; if first expression is true, the second expression is not evaluated. If first expression is false, then the outcome is the value of the second expression.
TITLE: While Loops
DESCRIPTION: While loops continue to loop back and run as long as the test expression is true. A loop that doesn't have a test expression is an infinite loop, or a bug, and the computer will get stuck. "Break" ends the loop and moves forward even if the test expression is still true.
TITLE: Troubleshooting
DESCRIPTION: When troubleshooting code, first look at the traceback (error code that can direct you to location and description of error). You can also use example code, check that it works, and then adapt to your needs. Test step by step (and test intermediate variables). Also, comment out different versions of code so you can compare what does and doesn't work.
"""
TEXT_LESSON_8 = """TITLE: Lists
DESCRIPTION: Lists are a sequence of anything; they don't have to be comprised of <i>just</i> characters or <i>just</i> numbers. You can even have <b>nested lists</b> where an expression in a list is another list. Use square brackets and separate the expressions by commas. A list of [] is an empty list. You can index a list and its expressions the same way that you do a string. If there is a nested list, you can index the expression (the list) and then the target item within the nested list.
TITLE: Mutation & Aliasing
DESCRIPTION: <b>Mutation</b> is the ability to change the original value of something by replacing it, and lists support mutation. Strings and numbers are not mutable; they create a new string and disassociate with the original. This makes it important to pay attention if multiple variables reference an object that you change. <b>Aliasing</b> references referring to one object in different ways. Again, if you change the object, it affects everything that references it. You can also <u>append</u> [list.append(element)], which is adding element to end of list and is mutation. You can concatenate lists with "+" and this produces a new list via assignment, not mutation. <u>Length</u> [len(list)] coubts the number of elements (outer elements only; not components of list-within-list) in a list or number of characters in a string.
TITLE: For Loops & Indexing in Lists
DESCRIPTION: <b>For loops</b> are a simpler way to do while loops for lists. "For name in list:" applies the block expression to each element (which is assigned the new name) until the end of the list. <b>Indexing</b> returns the first place in a list where the value occurs: list.index(value). It will return an error if the value isn't in the list. You can check if the value is in the list (T/F) with "print value in list".
"""



def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEXT_LESSON_1)
print generate_all_html(TEXT_LESSON_2)
print generate_all_html(TEXT_LESSON_3)
print generate_all_html(TEXT_LESSON_4)
print generate_all_html(TEXT_LESSON_5)
print generate_all_html(TEXT_LESSON_6)
print generate_all_html(TEXT_LESSON_7)
print generate_all_html(TEXT_LESSON_8)


