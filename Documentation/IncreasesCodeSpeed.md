> Increasing Code Speed
*A Tutorial*

**Changes:**
*13-04-22:* 9:47pm - Page Creation - StrScr 0.2.4:7

Yoo

You're here cause you're bored-
OR

You want faster code.

Well in this entry- You'll be taught different techniques for making code faster.


    For This Tutorial we'll be using the `PerformanceTest.str` example file!

    In a regular StarScript Install, OR Source Code Download-

    Check the **Scripts Host Directory**, Navigate to `Scripts` and PerformanceTest should be there.


**What is PerformanceTest.str**?
PerformanceTest.str (And it's revisions) is a code speed test, to test various techniques.

It's a huge, 9731ish line file that simply adds 1 to a variable.

Quick Note: **The Modified Versions are typically also in the Scripts folder. We won't make you type every optimisation out.**

**So~ What's the speed like for PerfTest?**

*Quick Note:* The Testing Computer is running a Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz   2.11 GHz

When __all alerts are on__ in the settings.json file:

*Quick Note:* I wouldn't recommend doing the All_Alerts_On tests on your own devices as- that many writes to a console can be damaging

**All_Alerts_On** - **StarScript For Python 0.2.4:7** - **Windows 11: Laptop Connected To Power** - 92.73 Seconds - Taken (9:57pm 13-04-22)

92.73 Seconds- is A LOT-
And that's connected to power-

**All_Alerts_On** - **StarScript For Python 0.2.4:7** - **Windows 11: Battery Saver Mode 💀** - 134.92 Seconds - Taken (10:00pm 13-04-22)

Some- VERY large times right there.

How shall we cut down on those times?

> **Step 1: Turn off settings.json alerts & cut down on prints.**
By turning off the settings.json alerts- We can cut down on a lot of run time.

In this case it doesn't apply but, Try not to overuse prints!

*Quick Note:* We've left "Timing" on so we can see runtimes.

**All_Alerts_Off** - **StarScript For Python 0.2.4:7** - **Windows 11: Laptop Connected To Power** - 7.53 Seconds - Taken (10:06pm 13-04-22)
**All_Alerts_Off** - **StarScript For Python 0.2.4:7** - **Windows 11: Battery Saver** - 17.59 Seconds - Taken (10:07pm 13-04-22)

As you can see, Simply disabling most of the console spam- really shrinks down the times!

Trimming down on prints, REALLY saves the times

For reference, We'll run a test of performance test, without it's small, constant spam of @Input
1.82 seconds for connected to power
6.15 seconds for battery saver.


So- As this clearly proves-

Simply removing the "say" command will, most of the time, decimate wait times.

But what about when the code is far bigger...

**Introducing MegaPerformanceTest**
135,857 lines.

If I leave my laptop, connected to power and leave the "tick" class as
```swift
class tick {
    @flag Input: raw

    func value {
        return @Input-- "@" means it's a flag to grab from
    }
    func add {
        say @Input
        @flag Value: raw
        @Input.set &math.add @Input, @Value
        say @Input
    }
}
```

The code- LITERALLY takes 149.83 seconds.
Keeping in mind, alerts are off.
*oh god what would the code be like with alerts on~*

If we change
```swift
func add {
        say @Input
        @flag Value: raw
        @Input.set &math.add @Input, @Value
        say @Input
    }
```
to
```swift
func add {
        -- say @Input -- (Print Statements are commented out)
        @flag Value: raw
        @Input.set &math.add @Input, @Value
        -- say @Input -- (Print Statements are commented out)
    }
```

It **STILL** takes a huge 28.17 seconds. (13/04/22 - 10:16pm)

*Safe to say this flawed tutorial covers the heaviest of optimsation.*

so this brings us to __step 2__
> **Step 2: Utilising Threading**
Threading is an amazing & 'easy' way to speed up projects!

*Quick Note:* Threading everything is a __horrible idea__.
            We conducteed a test where we changed EVERYTHING to be a new thread.
            This made the code take so long that we had to cancel the test as it had been
            4 minutes.

            Thread Responsibly!

If your code uses delays- That may be a reason for the slowing.

If the delays are essential but you still want fast speeds **AND OR** don't want your code stopping- Use Threads.

If you start a command with `thread<+>`- The command specified will run on a separate thread!

Use this with things such as function references!

Be careful though!