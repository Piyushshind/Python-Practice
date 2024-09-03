def bayes_theorem(prior_A, likelihood_B_given_A, prior_B):
   
    posterior_A_given_B = (likelihood_B_given_A * prior_A) / prior_B
    return posterior_A_given_B


prior_A = 0.01

likelihood_B_given_A = 0.99

prior_B = 0.02

posterior_A_given_B = bayes_theorem(prior_A, likelihood_B_given_A, prior_B)

print(f"The probability of having the disease given a positive test result is: {posterior_A_given_B:.4f}")
