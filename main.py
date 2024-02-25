def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = int(input('enter amount of male students: '))
    female = int(input('enter amount of female students: '))
    m_perc = (male/100) * 100
    f_perc = (female/100) * 100
    total = int(str(male)) + int(str(female))

    print(f'The total number of students: \t {total:3d}')
    print(f'The number of males and females \t {male:3d} \t {female:3d}')
    print(f'The percentage of males and females \t {m_perc:.2f} \t {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
