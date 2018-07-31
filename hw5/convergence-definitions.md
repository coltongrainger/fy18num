https://calculus.subwiki.org/wiki/Rate_of_convergence
https://creativecommons.org/licenses/by-sa/3.0/

\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}

TERM! Suppose $\lim_{n \to \infty} x_n = L$ and $\lim_{n \to \infty} \frac{|x_{n+1} - L|}{|x_n - L|} = \mu$, with $\mu \in (0,1)$. In this case, the sequence $(x_n)$ converges to $L$ [...]-ly, and the constant $\mu$ is called the rate of ([...]) convergence. The use of the term "[...]" signifies that the next error term $|x_{n+1} - L|$ is approximately a [...] function of the preceding error term $|x_n - L|$ ... linear

TERM! Suppose $\lim_{n \to \infty} x_n = L$ and $\lim_{n \to \infty} \frac{|x_{n+1} - L|}{|x_n - L|} = \mu$, with $\mu = 0$. In this case, the sequence $(x_n)$ converges to $L$ [...]. In other words, a function that would approximate the behavior of the next error term in terms of the previous error term would decay [...] than a linear function. ... superlinearly, faster

TERM! Suppose $\lim_{n \to \infty} x_n = L$ and $\lim_{n \to \infty} \frac{|x_{n+1} - L|}{|x_n - L|} = \mu$, with $\mu = 1$. In this case, the sequence $(x_n)$ converges to $L$ [...]. In other words, a function that would describe the next error term in terms of the previous one would decay [...] than a linear function. ... sublinearly, slower

DEF! Suppose $q > 1$ is a real number. We say that the sequence $(x_n)$ converges to a limit $L$ with order of convergence $q$ if the following holds: ... $\lim_{n \to \infty} \frac{|x_{n+1} - L|}{|x_n - L|^q} = \mu, \mu > 0$

ASSOC! Let $(x_n)$ be a sequence convergent to $L$, and suppose we have a function that approximately predicts $|x_{n+1} - L|$ in terms of $|x_n - L|$. What's the relation between the order of convergence $q$ of $(x_n)$ and this function? ... The function has a root of multiplicity $q$ at zero.

EXAMPLE! The sequence $e_n = (1/2)k^{n^2}$ has terms $1, 1/5, 1/625, \ldots$ and clearly converges to zero. But is it's order of convergence quadratic? (Hint: form $\lim_{n\to\infty}\abs{e_{n+1}}/\abs{e_n}^p$.) ... No? It's just superlinear.

EX! An iterative method having linear convergence (order of convergence $1$) might produce a sequence of errors [...] that is, the error is [action-verb] at each iteration. ... $1, 0.5, 0.25, \ldots$, halved/divided-by-$n$.

EX! An iterative method having quadratic convergence (order of convergence $2$) might produce a sequence of errors [...] that is, the error is [action-verb] at each iteration. ... $0.1, 0.01, 0.001, \ldots$, squared

EX! What's the order of convergence of $|e_n|=1/n$? sub-, super-, or linear? ... Sublinear. $$\frac{|e_{n+1}|}{|e_n|^p}=\frac{1/(n+1)}{1/n^p}=\frac{n^p}{n+1} \stackrel{\lim_{n\rightarrow\infty}}{\Longrightarrow} \left\{\begin{array}{cc}0 & p<1\\1 & p=1\\\infty & p>1\end{array}\right.$$ Only when $p=1$ will the limit be a constant $\mu=1$.

EX! What's the order of convergence of $|e_n|=1/2^n$? sub-, super-, or linear? ... Linear.$$\frac{|e_{n+1}|}{|e_n|^p}=\frac{2^{np}}{2^{n+1}} \stackrel{\lim_{n\rightarrow\infty}}{\Longrightarrow} \left\{\begin{array}{cc}0 & p<1\\1/2 & p=1\\\infty & p>1\end{array}\right.$$

!EX What's the order (find $p$ explicitly) of convergence of $|e_n|=1/2^{2^n}$? Terms begin $1/4,\; 1/16,\; 1/256,\;1/65536,\; \cdots$ ...
  Superlinear and quadratic. $$\frac{|e_{n+1}|}{|e_n|^p}=\frac{1/2^{2^{n+1}}}{(1/2^{2^n})^p} =\frac{(2^{2^n})^p}{2^{2^{n+1}}}=\frac{(2^{2^n})^p}{2^{2\times 2^n}} =\frac{(2^{2^n})^p}{(2^{2^n})^2} \stackrel{\lim_{n\rightarrow\infty}}{\Longrightarrow} \left\{\begin{array}{cc}0 & p<2\\1 & p=2\\\infty & p>2\end{array}\right.$$

FACT! There is a unique exponent $p\ge 0$, the order of convergence, so that $$\lim_{n\rightarrow\infty}\frac{|e_{n+1}|}{|e_n|^q}= \ldots$$ ... $$\left\{\begin{array}{cc}0 & q<p\\\mu & q=p\\\infty & q>p\end{array}\right.$$

