from dataclasses import dataclass, astuple


@dataclass
class DataMediator:
    def get_all_values(self) -> tuple:
        return astuple(self)


@dataclass
class Search:
    """Содержит текстовые значения блока поиска объявлений."""
    search_product: str = "Поиск по объявлениям"
    find: str = "Найти"


@dataclass
class Categories(DataMediator):
    """Содержит текстовые значения блока категорий объявлений."""
    clothes_shoes_accessories: str = "Одежда, обувь и аксессуары"
    transport: str = "Транспорт"
    work: str = "Работа"
    auto_parts: str = "Автозапчасти и аксессуары"
    for_home_garden: str = "Для дома и дачи"
    real_estate: str = "Недвижимость"
    service_offer: str = "Предложение услуг"
    hobby_leisure: str = "Хобби и отдых"
    electronics: str = "Электроника"
    product_for_children: str = "Товары для детей и игрушки"
    beauty_health: str = "Красота и здоровье"
    animals: str = "Животные"
    ready_business: str = "Готовый бизнес и оборудование"


@dataclass
class Transport(DataMediator):
    """Содержит текстовые значения объявлений о транспортах."""
    popular_cars: str = "Популярные легковые автомобили"
    cars: str = "Автомобили"
    rate_a_car: str = "Оценить авто"
    car_catalog: str = "Каталог авто"
    moto: str = "Мотоциклы и мототехника"
    special_vehicles: str = "Грузовики и спецтехника"
    water_transport: str = "Водный транспорт"
    spare_parts: str = "Запчасти и аксессуары"
    sale_contract: str = "Договор купли-продажи"


@dataclass
class Work(DataMediator):
    """Содержит текстовые значения объявлений о работе."""
    find_job: str = "Ищу работу"
    find_employee: str = "Ищу сотрудника"
    popular_jobs: str = "Популярные вакансии"
    field_of_activity: str = "Сфера деятельности"
    profession: str = "Профессия"
    schedule: str = "График работы"
    work_experience: str = "Опыт работы"
    including_candidates: str = "В том числе для кандидатов"
    salary: str = "Зарплата"
    payout_frequency: str = "Частота выплат"


@dataclass
class PopularJobs:
    """Содержит текстовые значения блока 'Популярные вакансии'."""
    administrator: str = "Администратор"
    driver: str = "Водитель"
    loader: str = "Грузчик"
    storekeeper: str = "Кладовщик"
    sales_representative: str = "Торговый представитель"
