import asta

file = 'id_allele1_allele2_probability.csv'

p_val, statistic, dof = asta.full_algorithm(file_path=file,
                                            cutoff_value=2.0,
                                            should_save_csv=True,
                                            should_save_plot=True)

print(p_val)
print(statistic)
print(dof)