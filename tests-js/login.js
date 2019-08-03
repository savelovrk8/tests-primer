
var webdriver = require('selenium-webdriver');
var By = webdriver.By;

var driver = new webdriver.Builder().forBrowser('chrome').build();

driver.get('http://localhost/litecart/admin/');

driver.findElement(By.name('username')).clear();
driver.findElement(By.name('username')).sendKeys('admin');

driver.findElement(By.name('password')).clear();
driver.findElement(By.name('password')).sendKeys('admin');

driver.findElement(By.name('login')).click();

// driver.quit();    // FIXME
