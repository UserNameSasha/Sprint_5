from selenium.webdriver.common.by import By


class Locators:
    #для регистрации нового пользователя
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,"//p[text()='Личный Кабинет']")#кнопка "Личный кабинет"
    REG_BUTTON = (By.XPATH,"//a[text()='Зарегистрироваться']")#кнопка "Зарегистрироваться"
    NAME = (By.XPATH,"(//input[@name='name'])[1]")#поле ввода "Имя"
    EMAIL = (By.XPATH,"(//input[@name='name'])[2]")#поле ввода "Email"
    PASSWORD = (By.XPATH,"//input[@type='password']")#поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']")#кнопка "Зарегистрироваться"
    REG_TEXT = (By.XPATH,"//p[text()='Такой пользователь уже существует']")#всплывающий текст при попытки повторной успешной регистрации
    ERROR_PASS = (By.XPATH,"//p[text()='Некорректный пароль']")#всплывающий текст при вводе некоректного пароля   

    #вход по кнопке «Войти в аккаунт» на главной странице для зарегистрированного пользователя
    ENTER_ACCOUNT_BUTTON = (By.XPATH,"//button[text()='Войти в аккаунт']")#кнопка "Войти в аккаунт"
    ENTER_ACCOUNT_TEXT_EMAIL = (By.XPATH,"//input[@type='text']")#Поле ввода 'Email'
    ENTER_ACCOUNT_TEXT_PASSWORD = (By.XPATH,"//input[@type='password']")#Поле ввода 'Пароль'
    ENTER_BUTTON = (By.XPATH,"//button[text()='Войти']")#кнопка 'Войти'
    ENTER_ACCOUNT_WIHT_ENTER_BUTTON = (By.XPATH,"//a[text()='Войти']")#кнопка "Войти" в форме регистрации
    ENTER_ACCOUNT_WIHT_PASSWORD_RECOVER = (By.XPATH,"//a[text()='Восстановить пароль']")#кнопка "Востановить пароль"
    ENTER_ACCOUNT_WIHT_ENTER_BUTTON_IN_PASSWORD_RECOVER = (By.XPATH,"//a[text()='Войти']")#копка "Войти в мнею востановления пароля"

    #Локаторы для перехода в разделы
    DESINGER_BUTTON = (By.XPATH,"//p[text()='Конструктор']")#кнопка "Конструктор"
    LOGO = (By.XPATH,"//div[@class='AppHeader_header__logo__2D0X2']")#логотип STELLAR BURGERS
    EXIT_BUTTON = (By.XPATH,"//button[text()='Выход']")#кнопка "Выход"

    #локаторы для разделов
    ROLLS_BUTTON = (By.XPATH,"//span[text()='Булки']")#булки
    BREAD = (By.XPATH,"(//p[text()='Флюоресцентная булка R2-D3'])[1]")#Флюоресцентная булка R2-D3(для проверки переходов по разделам)

    SAUCES_BUTTON = (By.XPATH,"//span[text()='Соусы']")#соусы
    SAUCES = (By.XPATH,"(//p[text()='Соус Spicy-X'])[1]")#Соус Spicy-X(для проверки переходов по разделам)

    FILLINGS_BUTTON = (By.XPATH,"//span[text()='Начинки']")#начинки
    FILLINGS = (By.XPATH,"(//p[text()='Говяжий метеорит (отбивная)'])[1]")#начинки Говяжий метеорит (отбивная)(для проверки переходов по разделам)

