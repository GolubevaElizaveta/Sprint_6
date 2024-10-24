class TestData:

    test_data_user1 = ['Лиза', 'Нарачинская', 'Космонавтов 20', 'Сокольники', '+79040146070', '24.10.2024', 'Холодновато']
    test_data_user2 = ['Ойро', 'Илосова', 'Рубинштейна 12', 'Лубянка', '+79781256478', '28.10.2024', 'Кататься']

    test_data_expected_answer = [
        [1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]