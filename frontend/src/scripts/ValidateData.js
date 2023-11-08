
/**
 * Make sure the given email has no invalid characters and is in proper email format.
 * Note that the characters !#$%&'*+-/=?^_`{|}~ are allowed in email addresses. Periods are allowed too, as long as they are not the first or last character and don't appear consecutively.
 * 
 * @param {string} email the email to be checked
 * @returns {boolean} true if the email is valid, false otherwise
 */
function isEmailValid(email) {
    var regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var matches = email.match(regex);
    return matches != null && matches.length >= 1;
}

/**
 * Make sure the given email isn't already in the list of emails.
 * 
 * @param {string} email the email to be checked
 * @param {Array} emailList the list of already used emails
 * @returns {boolean} true if the given email is not in emailList, false otherwise
 */
function isEmailUnique(email, emailList) {
    return !emailList.includes(email);
}

/**
 * Make sure the given username has no invalid characters.
 * Usernames must be between 6 and 20 characters inclusive. 
 * They can have any alphanumeric characters, along with periods, dashes and underscores. They can't start or end with a period.
 * 
 * @param {string} username the username to be checked
 * @returns {boolean} true if the username is valid, false otherwise
 */
function isUsernameValid(username) {
    var regex = /^(?=[a-zA-Z0-9._-]{6,20}$)[^.].*[^.]$/;
    var matches = username.match(regex);
    return matches != null && matches.length >= 1;
}

/**
 * Make sure the given username isn't already in the list of usernames.
 * 
 * @param {string} username the username to be checked
 * @param {Array} usernameList the list of already used usernames
 * @returns {boolean} true if the given username is not in usernameList, false otherwise
 */
function isUsernameUnique(username, usernameList) {
    return !usernameList.includes(username);
}

/**
 * Make sure the given input data is a number.
 * 
 * @param {string} num the data to be checked
 * @returns {boolean} true if the input data is a number, false otherwise
 */
function isNumeric(num) {
    return !isNaN(num);
}

/**
 * Make sure the given input data is an integer.
 * 
 * @param {string} num the data to be checked
 * @returns {boolean} true if the input data is an integer, false otherwise
 */
function isInteger(num) {
    return isNumeric(num) && Number.isInteger(parseFloat(num));
}

/**
 * Make sure the given input data is greater than or equal to 0.
 * 
 * @param {string} num the data to be checked
 * @returns {boolean} true if the input data is a number and is non-negative, false otherwise
 */
function isNonNegative(num) {
    return isNumeric(num) && parseInt(num) >= 0;
}

/**
 * Make sure the given input data is a non-negative integer.
 * 
 * @param {string} num the data to be checked
 * @returns {boolean} true if the input data is a non-negative integer, false otherwise
 */
function isNonNegativeInteger(num) {
    return isInteger(num) && isNonNegative(num);
}

/**
 * Checks if the given number is within the range given by the minimum and maximum values, inclusive.
 * @param {string} num 
 * @param {number} minimum 
 * @param {number} maximum 
 * @returns {boolean} true if the number is within the inclusive range, false otherwise
 */
function isNumberInRange(num, minimum, maximum) {
    return isNumeric(num) && parseFloat(num) >= minimum && parseFloat(num) <= maximum
}

/**
 * Make sure the given date is in yyyy-mm-dd format.
 * 
 * @param {string} date the date to be checked
 * @returns {boolean} true if the given date is in yyyy-mm-dd format
 */
function isDateValid(date) {
    var dateInfo = date.split('-');
    if (dateInfo.length === 3) {
        [yyyy, mm, dd] = dateInfo;
        return isNonNegativeInteger(yyyy) &&
               isNumberInRange(mm, 0, 11) &&
               isNonNegativeInteger(dd) &&
               isDayInMonthValid(dd, mm, yyyy);
    }
}

/**
 * Checks if the given day, month, and year make up a valid date.
 * 
 * @param {number} dd 
 * @param {number} mm 
 * @param {number} yyyy
 * @returns {boolean} true if the given day, month, and year make up a valid date, false otherwise
 */
function isDayInMonthValid(dd, mm, yyyy) {
    var year = parseInt(yyyy);
    var month = parseInt(mm);
    var day = parseInt(dd);
    var isLeapYear = year % 4 === 0 && (year % 100 !== 0 || (year % 100 === 0 && year % 400 === 0));
    monthsWith30Days = [4, 6, 9, 11];
    monthsWith31Days = [1, 3, 5, 7, 8, 10, 12];

    var dateMap = {};
    dateMap[2] = isLeapYear ? 29 : 28;
    for (var m in monthsWith30Days) {
        dateMap[monthsWith30Days[m]] = 30;
    }
    for (var m in monthsWith31Days) {
        dateMap[monthsWith31Days[m]] = 31;
    }
    console.log(dateMap);
    return isNumberInRange(day, 1, dateMap[month]);
}