export function generateSalt() {
    return Math.random().toString(36).substr(2, 16);
  }
  
export function getHashedPassword(password, salt) {
  const CryptoJS = require('crypto-js');
  return CryptoJS.SHA256(password + salt).toString();
}

export function checkPassword(inputedPassword, storedPassword, salt) {
  var hashedPassword = getHashedPassword(inputedPassword, salt);
  return storedPassword == hashedPassword;
}