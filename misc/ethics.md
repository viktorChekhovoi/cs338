# Viktor Chekhovoi

## Scenario #1

### A. Ethical questions

* Should I report the bug?
  * What could be the legal consequences for me?
  * For could be the legal consequences for InstaToonz?
  * How could this affect laws surrounding bug reporting and copyright?

### B. Stakeholders and their rights

* InstaToonz: the music shared by their users is protected by DMCA, specifically by Circumvension of Access Controls and Reverse Engineering. In addition, their internal software and "trade secrets" are also protected.
* Users: InstaToonz's users deserve to have privacy and have their direct messages properly encrypted and protected.

### C. Missing information

* Do I, in this scenario, have the necessary funds to pay a lawyer, in the case where I report the bug and get sued by InstaToonz? I'll assume that's the case for this assignment.

### D. Possible actions

1. Report the bug: either using one of the coordinated vulnerability disclosure services, or by contacting InstaToonz directly. If the bug involves music copyright, I'd need to contact a copyright lawyer to check if uncovering the bug violates anti-circumvention laws.

2. Don't report the bug.

In this scenario, I don't think reporting the bug anonymously would be possible. If I decide to report the bug, it would likely be because I consider the violations of the users' safety a bigger issue than the potential consequences. Anonymous reporting might not be possible at all, wouldn't necessarily guarantee InstaToonz would even consider my report, and might still be traceable to me. Because of this, I won't consider it as an option.

### E. Guidance from ACM Code of Ethics

* The Code states that a professional should be honest and trustworthy, which includes providing information about potential problems to the appropriate parties (1.3). Since the users are a stakeholder in this situation, they should know about this bug or InstaToonz should resolve it. InstaToonz also isn't respecting the privacy of their users, which also violates the Code (1.6).

* Section 2.5 explicitly states that I should provide objective evaluations when necessary, and "any issues that might result in major risk must be reported to appropriate parties." This means that I should report this issue, and another section provides more moral justification: "computing professionals should not access another's computer system, software, or data without a reasonable belief that such an action would be authorized or a compelling belief that it is consistent with the public good" (2.8).

In my understanding, the ACM Code of Ethics says that I have the ethical right and even an obligation to report the bug, even if its means using unauthorized access.

### F. Recommended action

First, if the bug involves encryption or copyright protection, contact a copyright lawyer to find out if uncovering this bug puts me in violation of the anti-circumvention law in the US. If it doesn't, great! If it does, I (as a non-lawyer) think that the privacy risk warrants the violation of InstaToonz's copyright, so I would focus on collecting evidence of the bug's severity for when InstaToonz sues me.

Second, report the bug privately to InstaToonz. The problem doesn't state the method to do that, but since the last bug-reporter did so privately, I'm assuming there is a method. Reporting it to a coordinated vulnerability disclosure service would not be a good idea because of how critical the bug is.

Finally, prepare for lawsuits and investigations. Given how the previous bug report went, I can expect InstaToonz to sue me for just reporting the bug. The problem states it caused the person significant expense, but also drew a lot of attention, so a public fundraiser could help cover the costs. Similar to the previous lawsuit, I can expect InstaToonz to drop it eventually, especially since now there's a precedent. I could also expect them to ask for an FBI investigation, although, again, it's unlikely that it will go anywhere due the fact that the FBI has declined to pursue the investigation previously.

I could be in danger if if me uncovering the bug violates anti-circumvention laws and it's not protected by Free Use. However, the fact that the bug violates the privacy of hundreds of millions of people should be a good enough defense.

For InstaToonz, it could be argued that their treatment of bug reporters may have slowed down the discovery of this bug, which in turn greatly harmed their users. Because of this, they might be required to change their treatment of bug reports in the future or even establish a bug bounty program.

Given that the previous case was so significant, it's likely that this will also receive wide coverage. Because of this, if the company is based in the US, it could lead to new protections for bug reporters. These protections would make it easier for people to uncover bugs and report them privately.
