import numpy as np

# Step 1: Define the sensitivity vectors for each bucket and the covariance matrices
# Covariance matrix for each bucket (3 buckets example)
cov_bucket_1 = np.array([[0.10, 0.02], [0.02, 0.08]])
cov_bucket_2 = np.array([[0.07, 0.01], [0.01, 0.05]])
cov_bucket_3 = np.array([[0.12, 0.03], [0.03, 0.09]])

# Sensitivity vectors for each bucket
sensitivity_bucket_1 = np.array([0.6, 0.4])
sensitivity_bucket_2 = np.array([0.5, 0.5])
sensitivity_bucket_3 = np.array([0.7, 0.3])

# Step 2: Calculate the bucket-level capital requirements K_b
def calc_bucket_capital(cov_matrix, sensitivity_vector):
    return np.sqrt(sensitivity_vector.T @ cov_matrix @ sensitivity_vector)

K_b1 = calc_bucket_capital(cov_bucket_1, sensitivity_bucket_1)
K_b2 = calc_bucket_capital(cov_bucket_2, sensitivity_bucket_2)
K_b3 = calc_bucket_capital(cov_bucket_3, sensitivity_bucket_3)

print(f"Bucket-level capital requirements: K_b1={K_b1:.4f}, K_b2={K_b2:.4f}, K_b3={K_b3:.4f}")

# Step 3: Class-level aggregation using the correlation matrix between buckets
K_b_vector = np.array([K_b1, K_b2, K_b3])
correlation_matrix_class = np.array([[1.0, 0.5, 0.3],
                                     [0.5, 1.0, 0.4],
                                     [0.3, 0.4, 1.0]])

K_class = np.sqrt(K_b_vector.T @ correlation_matrix_class @ K_b_vector)
print(f"Class-level capital requirement: K_class = {K_class:.4f}")

# Step 4: Total-level capital requirement using the correlation matrix between classes
# (Assume 3 classes; this example aggregates just one class, but for completeness)
K_class_vector = np.array([K_class])  # Single class in this example, so no other classes are present.
correlation_matrix_total = np.array([[1.0]])  # Single class correlation

K_total = np.sqrt(K_class_vector.T @ correlation_matrix_total @ K_class_vector)
print(f"Total capital requirement: K_total = {K_total:.4f}")

# Step 5: Marginal Contribution to Risk (MCR) for each bucket in the class
MCR_class = (correlation_matrix_class @ K_b_vector) / K_class
print(f"Marginal Contribution to Risk (MCR) for each bucket: {MCR_class}")

# Step 6: Contribution to Risk (CR) for each bucket in the class
CR_class = K_b_vector * MCR_class
print(f"Contribution to Risk (CR) for each bucket: {CR_class}")

# Step 7: Verify that the sum of CR equals the class-level capital requirement
total_CR_class = np.sum(CR_class)
print(f"Total Contribution to Risk (CR) for the class: {total_CR_class:.4f}")

# Step 8: Marginal Contribution to Risk (MCR) for class-level capital in total
MCR_total = (correlation_matrix_total @ K_class_vector) / K_total
print(f"Marginal Contribution to Risk (MCR) for total: {MCR_total}")

# Step 9: Contribution to Risk (CR) for the class in the total capital requirement
CR_total = K_class_vector * MCR_total
print(f"Contribution to Risk (CR) for total: {CR_total}")

# Step 10: Verify that the sum of CR equals the total capital requirement
total_CR_total = np.sum(CR_total)
print(f"Total Contribution to Risk (CR) for total: {total_CR_total:.4f}")

