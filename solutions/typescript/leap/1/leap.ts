function isLeapYear(year: number) {
    const year4 = (year % 4) === 0
    const year100 = (year % 100) === 0
    const year400 = (year % 400) === 0
    const isLeapYear = year4 === year100 === year400
    return isLeapYear
}

export default isLeapYear