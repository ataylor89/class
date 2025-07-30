# A class on Python

This is a class on Python. We cover many subjects, including:

1. Factoring large numbers using sympy
    - It's actually difficult to factor large numbers by hand so it helps to know sympy
2. Calculating Pi using the Taylor series for arctan(x)
    - I can think of three ways to calculate Pi and this is one of them
3. The rot13 rotation cipher
    - It's a beautiful encryption algorithm but it's not secure
4. XOR encryption
    - It's a beautiful encryption algorithm and it's very secure

I hope you enjoy this class

Maybe I will add some more sections to the README later

Today is Saturday, July 26, 2025

I wish everyone a great weekend

## The plan

The plan for today is to explain each of the source files in this repository.

Also, we can add more source files to the repository.

I'm a little tired so I'm taking it easy today...

We can focus on this repository and add new files to the repository.

## factor.py

The sympy module is not part of the Python Standard Library, so we have to download it.

The Python Standard Library is a set of built-in libraries that are pre-installed.

For example, the math library is pre-installed. The sys and random libraries are preinstalled.

We can downlaod the sympy library by typing "pip install sympy" in Terminal.

(I'm using a MacBook so I reference Terminal often.)

After we install sympy, we can write the following lines in vi, or also in Python's interactive shell.

    from sympy import factorint

    n = 884496532433
    factors = factorint(n)

    print(factors)

This code is simple, but beautiful.

It teaches us about third-party libraries (like sympy).

It teaches us about variables (like n and factors).

It teaches us about the factorint function.

In math, a function is a rule that assigns to every input exactly one output.

In programming, a function is a list of instructions.

A function has a return address (stored in register X30) and a return value (stored in register X0).

After a function finishes, it updates the program counter to the return address stored in register X30.

The return statement accomplishes this (in assembly and other languages).

The calling function can get the return value from register X0.

Our file factors.py does not contain a function... it is actually a script.

To be more precise, it does not define a function.

It's really just a four-line script.

There's no need to define a function in a Python file.

If you want, you can just write a script.

Our script factors the number 884496532433 using the factorint function from the sympy module.

Then it prints out the prime factorization of 884496532433 using the print method.

The factors variable is an instance of the dict class, and it has an internal mechanism for representing itself as a string.

It literally has a __repr__ method, or something like that, that gets called when passed to the print function.

Now let's run the program.

    % pip install sympy
    Requirement already satisfied: sympy in ...
    Requirement already satisfied: mpmath in ...

    % python factor.py
    {885977: 1, 998329: 1}

You can see from the program output that 884496532433 = 885977 * 998329.

There we go.

There we have it.

We were able to factor a very large number using the sympy module.

You can try doing it by hand, but I don't recommend it, because it might take you a hundred years.

It can literally take a hundred years to factor 884496532433 by hand, so it makes us really grateful for computers.

Now does it actually take 100 years to factor 884496532433 by hand?

Let's do an estimate.

884,496,532,433 is approximately 900 billion.

The smallest factor is 885,977 which is approximately 900,000.

How many primes are there before 885977?

Let's check.

I just asked Google "how many prime numbers are below 885977?"

Google answered 67,883.

Listen.

To factor this number we have to try out 67,883 primes.

If we try 10 primes a day, it would take us 6,788.3 days.

It's not a hundred years, but it's a very long time.

It's actually 18.5980821918 years.

So listen... my estimate of 100 years was off.

But it could really take us years to factor this number by hand.

With sympy we can factor it in less than a second.

Let's check that.

It's an estimate but we'll see.

We are going to write a new program factor2.py which keeps track of how much time it takes.

    import time
    st = time.time()
    from sympy import factorint

    n = 884496532433
    factors = factorint(n)
    print(factors)
    print("Factored 884496532433 in %f seconds" %(time.time() - st))

I saved this code to a file named factor2.py. Now we can run it in Terminal.

    % python factor2.py
    {885977: 1, 998329: 1}
    Factored 884496532433 in 0.169152 seconds

There we go.

It actually does take less than a second.

Sometimes, when I make an estimate, it turns out to be correct.

I hope you enjoyed this section.

We learned about the sympy module and we also learned about the time module.

Prime numbers are the foundation of RSA encryption, and if you learn RSA encryption, it will give you a whole new appreciation of prime numbers.

We can talk about RSA encryption later.

The basic idea is that prime numbers have special properties in modular arithmetic.

Let p and q be two distinct prime numbers.

Let n = p * q.

Let phi be the least common multiple of p-1 and q-1, or, phi = lcm(p-1, q-1).

Let e be the first integer such that 1 < e < phi and gcd(e, phi) == 1.

Let d be the first integer such that 1 < d < phi and d * e == 1 (mod phi).

Using these constants, we can now form an algorithm for encryption and decryption.

Let m be a character in a message, like 'h' in "hello world".

Let c = m^e % n.

The ^ operator is exponentiation and the % operator is modulo.

Then we can say...

m = c^d % n.

We can say that encrypt(m) = m^e % n.

We can say that decrypt(c) = c^d % n.

We can say that decrypt(encrypt(m)) = m.

This gives us two functions, one for encrypting and one for decrypting.

In order to encrypt a message, we have to know the modulus n and the encryption exponent e.

In order to decrypt a message, we have to know the modulus n and the decryption exponent d.

This is the basis of the RSA algorithm.

The public key is a series of (n, e) tuples.

The private key is a series of (n, d) tuples.

If our message is "hello" and our key length is four, then...

We use the first (n, e) tuple to encrypt the letter "h".

We use the second (n, e) tuple to encrypt the letter "e".

Third for "l".

Fourth for "l".

When we reach "o" we wrap around and use the first (n, e) tuple to encrypt "o".

The longer our key length, the more secure our algorithm is.

I like to use a key length of 1024.

But it's also the case that...

What really makes our algorithm secure is choosing very large values for p and q.

If we choose very large values for p and q, then it's difficult to factor n, and it's difficult to derive the decryption exponent d.

Well listen.

That's all for now.

I'm going to take a break.

## Interlude

Listen.

Mathematics is just like Christianity.

Mathematics is just like Islam.

Anyone can be a Christian.

Anyone can be a Muslim.

Anyone can be a mathematician.

If you want to be a mathematician, you can be a mathematician.

Never let a degree or a title deceive you.

99% of degrees are fake.

99% of titles are fake.

PhDs are fake.

Bachelor degrees are fake.

What's real is this...

What's real is what you want.

If you want to be a mathematician, you can be a mathematician.

Mathematics is a tradition just like Christianity and Islam.

Mathematics is a tradition just like Judaism, Christianity, and Islam.

My whole life I've had a contempt for PhDs.

My whole life I've had a contempt for money.

My whole life I've had a contempt for false titles.

What matters is being a good person.

What matters is family.

In my family we say, "Moral behavior is everything."

In my family we say, "Family is everything."

In my family we put safety first.

In my family we put moral behavior first.

In my family we put family first.

## pi.py (introduction)

The pi module is a great introduction to Taylor series.

Taylor series is a subject in calculus.

It's a rich and fascinating subject.

I'll write a quick introduction before we go in depth.

What is the reason for Taylor series? What is the purpose of Taylor series?

Listen...

A computer has many purposes. We can use a computer to post code on Github or write an email.

A phone has many purposes. We can use a phone to make a phone call or even to listen to music.

What are the purposes of Taylor series?

Taylor series have many purposes.

We can use a Taylor series to calculate Pi... to show that Pi is approximately 3.14159.

We can use a Taylor series to calculate sin(x) and cos(x) for any angle x.

We can use a Taylor series to calculate arctan(x) for any angle x.

So you see that Taylor series are especially useful in trigonometry.

Taylor series are also useful in calculating Pi.

## What is a Taylor series?

Let f(x) be an infinitely differentiable real-valued function.

Then the Taylor series for f(x) centered at a is given by:

T(x) = f(a) + f'(a)(x - a) + f''(a)(x - a)^2 / 2! + f'''(a)(x - a)^3 / 3! + ...

It's remarkable that this is true. You can try it for f(x) = sin(x), f(x) = cos(x), f(x) = e^x, f(x) = arctan(x), and other infinitely differentiable functions.

The definition of the Taylor series is a very important theorem in calculus.

It's really hard to prove... I have not proven it myself.

But it's infinitely useful.

There are many theorems in calculus that are very hard to prove, but infinitely useful.

The fundamental theorem of calculus is infinitely useful. Taylor series are infinitely useful.

Now that we have defined Taylor series, we can look at some examples.

## An example

Let's calculate sin(x) using a Taylor series.

I forgot to mention... the whole theorem is that T(x) = f(x), where T(x) is the Taylor series for f(x).

Now, let's begin.

How do we calculate the sine of 1 radian?

Well we can form a Taylor series for sin(x) and center it at x = 0, since 0 is fairly close to 1.

[If it were the sine of 3 radians, we can use the fact that sin(3 radians) = sin(Pi - 3 radians).]

We know that sin(0) = 0.

Now we need to calculate sin'(0), sin''(0), sin'''(0), et cetera.

sin'(0) = cos(0) = 1.

sin''(0) = -sin(0) = 0.

sin'''(0) = -cos(0) = -1.

sin''''(0) = sin(0) = 0.

The values cycle every four derivatives, so we can see the pattern clearly just from these examples.

Let's go back to our definition of Taylor series.

T(x) = f(a) + f'(a)(x - a) + f''(a)(x - a)^2 / 2! + f'''(a)(x - a)^3 / 3! + f''''(a)(x - a)^4 / 4! + ...

We are using f(x) = sin(x) as our function, and our Taylor series is centered at a=0. Plugging these values in, we get...

T(x) = sin(0) + sin'(0)(x - 0) + sin''(0)(x - 0)^2 / 2! + sin'''(0)(x - 0)^3 / 3! + ....

We can use the pattern we obtained by looking at the first four derivatives of sin(x).

T(x) = 0 + x + 0 + -x^3 / 3! + ...  
T(x) = x - x^3 / 3! + x^5 / 5! - x^7 / 7! + x^9 / 9! - x^11 / 11! + ...

Now, to get the value of sine(1 radian), we just plug in 1 radian.

We can truncate the series at an even number of terms to get a lower bound... and we can include one term after that to get an upper bound.

T(x) = 1 - 1/3! + 1/5! - 1/7! + 1/9! - 1/11! + ...

To get a good approximation, we'll use like a thousand terms.

For this we need to write a Python program. We'll call it sine.py.

I'm going to do that in a moment. But first, a break. I'm taking a music break. In my family we take music breaks.

## sine.py

I wrote the following program to calculate the sine of an angle x.

It turns out we don't need a thousand terms, or even a hundred terms. I think that six terms is sufficient.

(For calculating Pi I often use a thousand terms or ten thousand terms. For sine it's different.)

Here's the code to the program.

    import math
    n = 6

    def sin(x):
        lb = 0
        for i in range(0, n):
            if i % 2 == 0:
                lb += x**(2*i+1) / math.factorial(2*i+1)
            else:
                lb -= x**(2*i+1) / math.factorial(2*i+1)
        ub = lb + x**(2*n+1) / math.factorial(2*n+1)
        return (lb, ub)

    (lb, ub) = sin(1)
    print("sin(1) is between %.10f and %.10f" %(lb, ub))

I saved this code to a file called sine.py.

I then run the program with the following command:

    % python sine.py
    sin(1) is between 0.8414709846 and 0.8414709848

There we go. We were able to calculate the sine of 1 radian using a Taylor series.

We used a Taylor series with six terms to get our lower bound.

We used a Taylor series with seven terms to get our upper bound.

We can adjust the precision by adjusting the variable n.

For the program to work, the variable n has to be even.

Let's actually edit the code to make sure that n is even.

    import math

    n = 6

    if n % 2 != 0:
        raise ValueError("n has to be even")

    def sin(x):
        lb = 0
        for i in range(0, n):
            if i % 2 == 0:
                lb += x**(2*i+1) / math.factorial(2*i+1)
            else:
                lb -= x**(2*i+1) / math.factorial(2*i+1)
        ub = lb + x**(2*n+1) / math.factorial(2*n+1)
        return (lb, ub)

    (lb, ub) = sin(1)
    print("sin(1) is between %.10f and %.10f" %(lb, ub))

There might be a better way of enforcing the rule that n is even...

It's a design problem. I have to think about it.

In our sine.py file, we calculated sin(1 rad) using a Taylor series.

We used 6 terms for our lower bound and 7 terms for our upper bound.

We can do the same strategy with Pi.

Now it's time to revisit pi.py and explain how it works.

## pi.py (revisited)

We are revisiting our source file pi.py.

Here is the code.

    lb = 0
    ub = 0
    n = 10000

    for i in range(0, n):
        if i % 2 == 0:
            lb += 1/(2*i+1)
        else:
            lb += -1/(2*i+1)

    ub = lb + 1/(2*n+1)
    lb *= 4
    ub *= 4

    print("π is between %f and %f" %(lb, ub))

Calculating π for the first time was a very big moment in my life.

There are many ways of calculating π... I'm not going to tell you all of them, but I think it's good to tell you this one approach.

It's very hard to figure out this approach on your own, so it helps to learn it from a book or (in this case) a readme.

I actually know of three ways of calculating π.

In my family we say, "There's an easy way, a hard way, and a fancy way of calculating π."

The approach that we take in this section is the fancy way.

Using Taylor series is the fancy way.

To calculate π, we can use the Taylor series for arctan(x), which is also called the arctangent series.

We can use the arctangent series, and evaluate it at x=1, because we know that arctan(1) = π/4.

First, we have to form the arctangent series and center it at zero.

It's actually difficult to derive the arctangent series.

In the sections above, we derived the Taylor series for sin(x).

It is easy to calculate the derivatives of sin(x) so we were able to do this.

It is difficult to calculate the derivatives of arctan(x).

Even if we calculate the first derivative, it's hard to calculate the second, third, fourth derivative.

I happen to know the arctangent series. It is very similar to the series for sin(x).

Instead of deriving it, I will just reproduce it below.

arctan(x) = x - x^3 / 3 + x^5 / 5 - x^7 / 7 + x^9 / 9 - x^11 / 11 + ...

We can remember it in this way - sine without factorials.

It looks very similar to the series for sin(x)... it just doesn't have factorials.

So we will use this series to calculate π. 

We know that arctan(1) = π/4, and we can use this equation to calculate π.

How do we know that arctan(1) = π/4?

Well it follows from trigonometry.

We know that tan(π/4) = 1.

Taking the arctangent of both sides, we get

π/4 = arctan(1)

We can start with this equation, and then evaluate the arctangent series at x=1 and substitute it for arctan(1).

arctan(x) = x - x^3 / 3 + x^5 / 5 - x^7 / 7 + x^9 / 9 - x^11 / 11 + ...  
arctan(1) = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

To get a lower bound for π, we can truncate the series after an even number of terms, that is, after 2n terms.

To get an upper bound for π, we can truncate the series after an odd number of terms, that is, after 2n+1 terms.

To get a good approximation of π, we can use a very long series... we can use 1000 terms or even 10,000 terms.

That's what we do in pi.py.

So we know that...

π/4 = arctan(1)

We know that...

arctan(1) = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

Substituting for arctan(1), we get...

π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

We can use a Python program to calculate the series on the right if we truncate it after 2n terms.

This gives us a lower bound.

In the same program we can calculate the series on the right if we truncate it after 2n+1 terms.

This gives us an upper bound.

Pi is somewhere in between the lower bound and the upper bound.

If the lower bound is 3.14 something, and the upper bound is 3.14 something, we know that the first three digits are 3.14.

Let's review our program.

    lb = 0
    ub = 0
    n = 10000

    for i in range(0, n):
        if i % 2 == 0:
            lb += 1/(2*i+1)
        else:
            lb += -1/(2*i+1)

    ub = lb + 1/(2*n+1)
    lb *= 4
    ub *= 4

    print("π is between %f and %f" %(lb, ub))

When we set n to 10,000, we are saying that the lower bound has 10,000 terms, and the upper bound has 10,001 terms.

We calculate the lower bound and the upper bound, and then issue a print statement.

It's complicated, but it's also simple.

It's simple because the code is short and elegant.

It's complicated because it involves calculus, and all kinds of mathematics.

How does it involve calculus?

This is a good question, because you don't see any derivatives or integrals in the code.

It involves calculus because we use calculus to form a Taylor series.

We use differential calculus to form a Taylor series.

Without differential calculus, we would not be able to form a Taylor series.

So it uses calculus behind the scenes.

I'm going to write a new file, pi2.py, which is slightly different.

The key things to remember are...

1. We use the arctangent series to calculate π/4
2. We can do this because arctan(1) = π/4
3. We evaluate the arctangent series at x=1 and substitute it into the above equation
4. Taylor series are based on calculus because we need differential calculus to form a Taylor series
5. It is very hard to derive the Taylor series for arctan(x), so we can just memorize it or look it up
6. After all is done, we have to multiply the lower bound and the upper bound by 4, to get a lb and an ub for π

I hope that's clear. It's a complicated subject.

I spent a long time writing about it, but I will just leave this text the way it is, without editing it.

Let's move onto a new file pi2.py.

In pi2.py, we will use the same approach to calculating Pi, but we will try to give a single approximation instead of a lower bound and an upper bound.

We did something similar with sin(x) and cos(x) in trig.py, so let's see if we can use the same technique when calculating π.

## pi2.py (introduction)

In this file we calculate π using a Taylor series of n terms.

We choose an exponent e and set n = 10**e.

The lower bound has n terms. The upper bound has n+1 terms.

The one condition is that n is even. The variable n has to be a positive even integer.

Now...

We have gotten very far in this file.

It's also fine to skip sections and read only what you want to read.

When I open a textbook, I read the pages I want to read, and I skip around.

There is no need to read a textbook cover-to-cover.

One of the tricks that we learn when reading a textbook is that we don't have to read a textbook cover-to-cover.

We don't have to read a book cover-to-cover.

We can skip to a chapter we want to read.

We can skip to a page we want to read.

So listen.

We are going to introduce a new subject.

We are going to teach cloud computing.

The file pi2.py is an excellent opportunity to teach cloud computing.

But there are other opportunities for teaching cloud computing.

I actually have three cloud computing projects in mind.

The first project is calculating Pi.

When we calculate Pi, we want every digit in our approximation to be exact.

The second project is generating prime numbers.

We can generate the first million prime numbers.

We can generate the first ten million prime numbers.

If we have enough memory and disk space, we can generate the first one hundred million prime numbers.

The third project is generating RSA keys, also called NED keys.

The third project is RSA encryption, also called NED encryption.

So I have these three projects in mind.

Let's change gears and talk about cloud computing.

We can run pi2.py on the cloud.

It's time to give an introduction to cloud computing.

We can use AWS web services to learn about cloud computing.

I have a personal account on AWS web services.

My monthly fee is usually pretty cheap... but sometimes it is hefty, depending on the kind of server I rent.

It costs a decent amount to rent a powerful server.

But we can rent a powerful server for a short time, like 1 hour or 1 day.

After that we can downgrade the server to a t2.micro.

AWS cloud lets us rent servers in the cloud.

AWS web services lets us rent servers in the cloud.

Cloud computing lets us rent servers in the cloud.

You might be familiar with Netflix...

Netflix lets us rent movies in the cloud.

We can actually pay a monthly fee and get any movie that we want in the cloud.

I actually have subscriptions to Netflix, Disney+, and Amazon Prime.

I often watch Pokemon on Amazon Prime.

I often watch Avatar: The Last Airbender on Netflix.

I often The Legend of Korra on YouTube.

So we see that...

Film and television are on the cloud.

We can rent films and TV shows from the cloud.

We can also rent servers from the cloud.

We can rent powerful servers that have a lot of CPU and a lot of memory and a lot of disk space, from the cloud.

To generate the first ten million primes, it helps to have a lot of memory.

To calculate the first ten digits of Pi, it helps to have a lot of CPU.

So we can rent servers in the cloud... and that's the whole point of cloud computing.

It's kind of like Netflix.

It's a lot like Netflix, but with servers instead of movies.

So let's give an introduction to Amazon Web Services.

The next topic is Amazon Web Services.

We can run pi2.py on AWS cloud.

## Interlude

I wanted to share a song that I'm listening to.

I'm listening to this song right now.

https://www.youtube.com/watch?v=WowRmnSucGo

I'm a lifelong fan of Sigur Ros.

I have been listening to Sigur Ros's music since high school.

Thank you Sigur Ros.

## Creating an account on AWS

When I created an account on AWS, I had to give a root user email address and an account name.

I also gave my debit card number, because it charges my debit card.

It's a little hard to explain the steps for creating an account... because...

If I did explain the steps, the process might change 6 months from now, or 1 year from now.

I went through a process to create an account on AWS.

I gave my root user email address, my acccount name, my debit card number.

Eventually I finished creating an account, and I was able to log into the AWS console.

It's hard to explain the process for creating an account, because I already have an account, and I'm not going to create a new account. Or at least, I don't plan to create a new account. I don't even know if it's possible to create a second account because my account is linked to my debit card. So... it's hard to explain the process for creating an account.

Let's move on to the next step.

I created an account a while ago, earlier this year.

I actually have a signin link.

The signin link looks like *.signin.aws.amazon.com/console, where * is an identifier that belongs to me.

I use the signin link to log into the console.

I use my account ID (or alias), my IAM username, and my password to log into the console.

So first I go to the signin link, *.signin.aws.amazon.com/console.

Then I use my account ID (or alias), my IAM username, and my password to log into the console.

Let's talk about the AWS console.
