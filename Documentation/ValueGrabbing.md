> Value Grabbing

**Changes:**
*02-04-22:* 3:35pm - Page Creation

You may have noticed that in function-running- the attached flags may start with certain symbols.
```java
makeWindow Name: @Name, Title: @Title, Size: @Size
```
for example, Uses "@" signs.

*So what's this about?*:
    When attaching a flag- In most cases you'll have to specify what type of flag that is.

    In most cases- StarScript will check multiple different areas, with the given command and will determine what it is, using that method- HOWEVER

    In some cases, such as, assigning a value,

    StarScript will need to be **told what the value is**

*So what are the value types?*:
    `<Raw>` - Just raw text.
    `@<Flag>` - Grabs value from a Flag (Or Class Variable)
    `#<InputName>` - Asks user for input with the text after '#'

Enjoy!