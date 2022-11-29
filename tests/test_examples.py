from data.search import (Categories,
                         Transport,
                         Work,
                         PopularJobs)


def test_search_product(main_page):
    """Проверка отображения объявлений после поиска."""
    main_page.advertisements_search("iphone 13 pro")
    assert main_page.check_advt_displayed()


def test_choose_transport_category(main_page):
    """Проверка отображения объявлений по категории автомобили."""
    assert main_page.check_categories()

    main_page.choose_category(Categories.transport)
    assert main_page.check_located_elements_by_text(*Transport().get_all_values())

    main_page.click_by_text(Transport.cars)
    assert main_page.check_advt_displayed()


def test_add_favorites(work_page):
    """Проверка добавления объявления в избранное."""
    work_page.click_by_text(Work.find_job).\
        click_by_text(PopularJobs.sales_representative)
    assert work_page.check_located_elements_by_text(Work.field_of_activity,
                                                    Work.profession,
                                                    Work.schedule,
                                                    Work.work_experience,
                                                    Work.including_candidates,
                                                    Work.salary,
                                                    Work.payout_frequency)
    assert work_page.check_advt_displayed()

    first_title_name = work_page.get_first_advt_title()
    work_page.add_favorites_first_advt() \
        .open_favorites()
    assert work_page.check_located_elements_by_text(first_title_name)
