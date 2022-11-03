import os

import pandas as pd
from django.test import TestCase
from pandas import Timestamp
from pandas.testing import assert_frame_equal

from polls.logic import read_csv, read_xml, merge_data, filter_data


class DataCollectionTest(TestCase):
    def test_read_csv(self):
        data = [{'username': 'M.Steam', 'password': 'ASDf43f#$dsD',
                 'date_joined': Timestamp('2021-12-05 10:42:12+0000', tz='UTC')},
                {'username': 'V.Markus', 'password': 'DSA4FSFF54w%$#df',
                 'date_joined': Timestamp('2016-05-23 14:46:57+0000', tz='UTC')},
                {'username': 'M.Stone', 'password': 'Lkds(*dsdadf',
                 'date_joined': Timestamp('2016-06-16 12:09:33+0000', tz='UTC')},
                {'username': 'A.Mecman', 'password': 'MKds#$DSd',
                 'date_joined': Timestamp('2015-07-23 10:21:51+0000', tz='UTC')},
                {'username': 'A.Mechailov', 'password': '35050Dsa',
                 'date_joined': Timestamp('2020-04-17 17:52:49+0000', tz='UTC')},
                {'username': 'V.Jmishenko', 'password': 'MDsa4wtwefS',
                 'date_joined': Timestamp('2014-02-09 05:49:44+0000', tz='UTC')},
                {'username': 'H.Snom', 'password': 'DSA3r34tdfsFd',
                 'date_joined': Timestamp('2018-04-08 00:35:37+0000', tz='UTC')},
                {'username': 'Stus', 'password': 'DAScaf34gDF4%',
                 'date_joined': Timestamp('2015-01-13 15:02:16+0000', tz='UTC')},
                {'username': None, 'password': None, 'date_joined': None},
                {'username': None, 'password': 'FASf4gsdcsDS54', 'date_joined': None},
                {'username': 'I.Lok', 'password': None, 'date_joined': Timestamp('2019-12-07 00:24:44+0000', tz='UTC')},
                {'username': 'Mavic', 'password': 'MK43trfDSv',
                 'date_joined': Timestamp('2018-04-23 18:48:31+0000', tz='UTC')},
                {'username': 'A.', 'password': 'fDSavIUDasf', 'date_joined': None},
                {'username': 'K.hex', 'password': 'mkSArwefd',
                 'date_joined': Timestamp('2015-06-30 21:27:47+0000', tz='UTC')}]

        df = pd.DataFrame(data)
        file_path = (os.path.dirname(__file__)) + "/test_task.csv"
        csv_file = open(file_path)
        assert_frame_equal(read_csv(csv_file), df)

    def test_read_xml(self):
        data = [{'first_name': 'Anton', 'last_name': 'Mechailov',
                 'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg'},
                {'first_name': 'Valerii', 'last_name': 'Jmishenko',
                 'avatar': 'https://static.boredpanda.com/blog/wp-content/uploads/2017/04/Virrappan2-58f79980ae6fb__880.jpg'},
                {'first_name': 'McMarry', 'last_name': 'Stone',
                 'avatar': 'https://photos.lensculture.com/large/5dd2fa6e-fe8d-469f-959b-46299ced511d.jpg'},
                {'first_name': None, 'last_name': 'Mavic',
                 'avatar': 'https://cdn.ebaumsworld.com/mediaFiles/picture/2260628/84557512.jpg'},
                {'first_name': 'Artur', 'last_name': None,
                 'avatar': 'http://farm4.static.flickr.com/3134/2371236790_8f973e4469.jpg'},
                {'first_name': None, 'last_name': None,
                 'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/15345c41332353.57a1ce9141249.jpg'}]

        df = pd.DataFrame(data)
        file_path = (os.path.dirname(__file__)) + "/test_task.xml"
        xml_file = open(file_path)
        assert_frame_equal(read_xml(xml_file).reset_index(drop=True), df.reset_index(drop=True))

    def test_merge_data(self):
        csv_data = [{'username': 'M.Steam', 'password': 'ASDf43f#$dsD',
                     'date_joined': Timestamp('2021-12-05 10:42:12+0000', tz='UTC')},
                    {'username': 'V.Markus', 'password': 'DSA4FSFF54w%$#df',
                     'date_joined': Timestamp('2016-05-23 14:46:57+0000', tz='UTC')},
                    {'username': 'M.Stone', 'password': 'Lkds(*dsdadf',
                     'date_joined': Timestamp('2016-06-16 12:09:33+0000', tz='UTC')},
                    {'username': 'A.Mecman', 'password': 'MKds#$DSd',
                     'date_joined': Timestamp('2015-07-23 10:21:51+0000', tz='UTC')},
                    {'username': 'A.Mechailov', 'password': '35050Dsa',
                     'date_joined': Timestamp('2020-04-17 17:52:49+0000', tz='UTC')},
                    {'username': 'V.Jmishenko', 'password': 'MDsa4wtwefS',
                     'date_joined': Timestamp('2014-02-09 05:49:44+0000', tz='UTC')},
                    {'username': 'H.Snom', 'password': 'DSA3r34tdfsFd',
                     'date_joined': Timestamp('2018-04-08 00:35:37+0000', tz='UTC')},
                    {'username': 'Stus', 'password': 'DAScaf34gDF4%',
                     'date_joined': Timestamp('2015-01-13 15:02:16+0000', tz='UTC')},
                    {'username': None, 'password': None, 'date_joined': None},
                    {'username': None, 'password': 'FASf4gsdcsDS54', 'date_joined': None},
                    {'username': 'I.Lok', 'password': None,
                     'date_joined': Timestamp('2019-12-07 00:24:44+0000', tz='UTC')},
                    {'username': 'Mavic', 'password': 'MK43trfDSv',
                     'date_joined': Timestamp('2018-04-23 18:48:31+0000', tz='UTC')},
                    {'username': 'A.', 'password': 'fDSavIUDasf', 'date_joined': None},
                    {'username': 'K.hex', 'password': 'mkSArwefd',
                     'date_joined': Timestamp('2015-06-30 21:27:47+0000', tz='UTC')}]
        csv_data = pd.DataFrame(csv_data)
        xml_data = [{'user_id': 1, 'first_name': 'Anton', 'last_name': 'Mechailov',
                     'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg'},
                    {'user_id': 54, 'first_name': 'Valerii', 'last_name': 'Jmishenko',
                     'avatar': 'https://static.boredpanda.com/blog/wp-content/uploads/2017/04/Virrappan2-58f79980ae6fb__880.jpg'},
                    {'user_id': 10, 'first_name': 'McMarry', 'last_name': 'Stone',
                     'avatar': 'https://photos.lensculture.com/large/5dd2fa6e-fe8d-469f-959b-46299ced511d.jpg'},
                    {'user_id': 12, 'first_name': None, 'last_name': 'Mavic',
                     'avatar': 'https://cdn.ebaumsworld.com/mediaFiles/picture/2260628/84557512.jpg'},
                    {'user_id': 75, 'first_name': 'Artur', 'last_name': None,
                     'avatar': 'http://farm4.static.flickr.com/3134/2371236790_8f973e4469.jpg'},
                    {'user_id': 4234, 'first_name': None, 'last_name': None,
                     'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/15345c41332353.57a1ce9141249.jpg'}]

        xml_data = pd.DataFrame(xml_data)
        data = [{'username': 'V.Markus', 'password': 'DSA4FSFF54w%$#df',
                 'date_joined': Timestamp('2016-05-23 14:46:57+0000', tz='UTC'), 'user_id': 1, 'first_name': 'Anton',
                 'last_name': 'Mechailov',
                 'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg'}]

        df = pd.DataFrame(data)
        assert_frame_equal(merge_data(csv_data, xml_data), df)

    def test_filter_data(self):
        xml_data = [{'user_id': 6, 'first_name': 'Max', 'last_name': 'St(dsa53d)eam',
                     'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'},
                    {'user_id': 1, 'first_name': 'Anton', 'last_name': 'Mechailov',
                     'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg'},
                    {'user_id': 54, 'first_name': 'Valerii', 'last_name': 'Jmishenko',
                     'avatar': 'https://static.boredpanda.com/blog/wp-content/uploads/2017/04/Virrappan2-58f79980ae6fb__880.jpg'},
                    {'user_id': 47, 'first_name': '(Mov)', 'last_name': 'Stus',
                     'avatar': 'https://i.ytimg.com/vi/sgVHzNwthC0/maxresdefault.jpg'},
                    {'user_id': 23, 'first_name': 'Valeria (MSDAD ds 32d das)', 'last_name': 'Markus',
                     'avatar': 'https://live.staticflickr.com/5252/5403292396_0804de9bcf_b.jpg'},
                    {'user_id': 10, 'first_name': 'McMarry', 'last_name': 'Stone',
                     'avatar': 'https://photos.lensculture.com/large/5dd2fa6e-fe8d-469f-959b-46299ced511d.jpg'},
                    {'user_id': 85, 'first_name': 'Anton', 'last_name': 'Mecman( das (dsa ) )',
                     'avatar': 'https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/506829/original/Photo_on_2009-09-20_at_18.23_4/make-funny-faces-and-random-noises-to-random-people.jpg'},
                    {'user_id': 123, 'first_name': 'Wi(54)ll', 'last_name': 'Terman',
                     'avatar': 'https://i.pinimg.com/736x/e6/09/16/e609168f9d1daec1b16be6a1832a2dd7.jpg'},
                    {'user_id': 12, 'first_name': None, 'last_name': 'Mavic',
                     'avatar': 'https://cdn.ebaumsworld.com/mediaFiles/picture/2260628/84557512.jpg'},
                    {'user_id': 75, 'first_name': 'Artur', 'last_name': None,
                     'avatar': 'http://farm4.static.flickr.com/3134/2371236790_8f973e4469.jpg'},
                    {'user_id': 10, 'first_name': 'Ko(SELECT name FROM user;)lin', 'last_name': 'Hex',
                     'avatar': 'https://www.randomlists.com/img/people/john_bon_jovi.webp'},
                    {'user_id': 4234, 'first_name': None, 'last_name': None,
                     'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/15345c41332353.57a1ce9141249.jpg'}]

        xml_data = pd.DataFrame(xml_data)

        data = [{'user_id': 1, 'first_name': 'Anton', 'last_name': 'Mechailov',
                 'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/35af6a41332353.57a1ce913e889.jpg'},
                {'user_id': 54, 'first_name': 'Valerii', 'last_name': 'Jmishenko',
                 'avatar': 'https://static.boredpanda.com/blog/wp-content/uploads/2017/04/Virrappan2-58f79980ae6fb__880.jpg'},
                {'user_id': 10, 'first_name': 'McMarry', 'last_name': 'Stone',
                 'avatar': 'https://photos.lensculture.com/large/5dd2fa6e-fe8d-469f-959b-46299ced511d.jpg'},
                {'user_id': 12, 'first_name': None, 'last_name': 'Mavic',
                 'avatar': 'https://cdn.ebaumsworld.com/mediaFiles/picture/2260628/84557512.jpg'},
                {'user_id': 75, 'first_name': 'Artur', 'last_name': None,
                 'avatar': 'http://farm4.static.flickr.com/3134/2371236790_8f973e4469.jpg'},
                {'user_id': 4234, 'first_name': None, 'last_name': None,
                 'avatar': 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/15345c41332353.57a1ce9141249.jpg'}]

        df = pd.DataFrame(data)
        assert_frame_equal(filter_data(xml_data), df)
