from selenium.webdriver.common.by import By


class Locators:
    #для регистрации нового пользователя
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,"(//header//p)[3]")#кнопка "Личный кабинет"
    REG_BUTTON = (By.XPATH,"//*[@id='root']/div/main/div/div/p[1]/a")#кнопка "Зарегистрироваться"
    NAME = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")#поле ввода "Имя"
    EMAIL = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")#поле ввода "Email"
    PASSWORD = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input")#поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH,"//*[@id='root']/div/main/div/form/button")#кнопка "Зарегистрироваться"
    REG_TEXT = (By.XPATH,"//*[@id='root']/div/main/div/p")#всплывающий текст при попытки повторной успешной регистрации
    ERROR_PASS = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[3]/div/p")#всплывающий текст при вводе некоректного пароля   

    #вход по кнопке «Войти в аккаунт» на главной странице для зарегистрированного пользователя
    ENTER_ACCOUNT_BUTTON = (By.XPATH,"//*[@id='root']/div/main/section[2]/div/button")#кнопка "Войти в аккаунт"
    ENTER_ACCOUNT_TEXT_EMAIL = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")#Поле ввода 'Email'
    ENTER_ACCOUNT_TEXT_PASSWORD = (By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")#Поле ввода 'Пароль'
    ENTER_BUTTON = (By.XPATH,"//*[@id='root']/div/main/div/form/button")#кнопка 'Войти'
    ENTER_ACCOUNT_WIHT_ENTER_BUTTON = (By.XPATH,"//*[@id='root']/div/main/div/div/p/a")#кнопка "Войти" в форме регистрации
    ENTER_ACCOUNT_WIHT_PASSWORD_RECOVER = (By.XPATH,"//*[@id='root']/div/main/div/div/p[2]/a")#кнопка "Востановить пароль"
    ENTER_ACCOUNT_WIHT_ENTER_BUTTON_IN_PASSWORD_RECOVER = (By.XPATH,"//*[@id='root']/div/main/div/div/p/a")#копка "Войти в мнею востановления пароля"

    #Локаторы для перехода в разделы
    DESINGER_BUTTON = (By.XPATH,"//*[@id='root']/div/header/nav/ul/li[1]/a/p")#кнопка "Конструктор"
    LOGO = (By.XPATH,"//*[@id='root']/div/header/nav/div/a")#логотип STELLAR BURGERS
    EXIT_BUTTON = (By.XPATH,"//*[@id='root']/div/main/div/nav/ul/li[3]/button")#кнопка "Выход"

    #локаторы для разделов
    ROLLS_BUTTON = (By.XPATH,"//*[@id='root']/div/main/section[1]/div[2]/h2[1]")#булки
    SAUCES_BUTTON = (By.XPATH,"//*[@id='root']/div/main/section[1]/div[2]/h2[2]")#соусы
    FILLINGS_BUTTON = (By.XPATH,"//*[@id='root']/div/main/section[1]/div[2]/h2[3]")#начинки