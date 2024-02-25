def main():
    
    male = int(input('enter amount of male students: '))
    female = int(input('enter amount of female students: '))
    total = male + female 

    print(f'The total number of students \t \t {total:3d}')
    print(f'The number of males and females \t {male:3d} \t {female:3d}')

    m_perc= (male/total)* 100
    f_perc= (female/total)* 100
    print(f'The percentage of males and females \t {m_perc:.2f}% \t {f_perc:.2f}%')
    
    return m_perc, f_perc


if __name__ == '__main__':
    main()
