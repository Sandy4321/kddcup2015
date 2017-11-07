#-*-coding:utf-8-*-

import log
import datetime
import numpy as np

class EnrollmentFT:
    def __init__(self):
        self.user_course = {}
        self.log_time = {}
        #self.UCFeature = []
        log_info = log.LogInfo('../data/train/log_train.csv').enrollment_info

        event = ('problem', 'video', 'access', 'wiki', 'discussion', 'navigate', 'page_close')
        source = ('server', 'browser')

        for enrollment in log_info:
            log_num = 0
            log_num_last_oneweek = 0
            log_num_last_twoweek = 0
            source_sts = [0, 0]
            event_sts = [0 for x in range(0, 7)]
            day_num = 1 #登录天数
            #time_per_day = [] #每天学习时长
            day_interval = [] #两次登录间隔天数
            t_begin = datetime.datetime.strptime(log_info[enrollment][0][0], '%Y-%m-%dT%H:%M:%S')
            t_end = datetime.datetime.strptime(log_info[enrollment][-1][0], '%Y-%m-%dT%H:%M:%S')
            span = (t_end - t_begin).days + 1
            log_list = []

            for row in log_info[enrollment]:
                source_sts[source.index(row[1])] += 1
                event_sts[event.index(row[2])] += 1
                log_num += 1
                t = datetime.datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
                # if((t_end - t).days <= 7):
                #     log_num_last_oneweek +=1
                #     log_num_last_twoweek += 1
                # elif((t_end - t).days <= 14):
                #     log_num_last_twoweek += 1
                if(log_info[enrollment].index(row) != 0):
                    last_span = t.day - t_last.day + (t.month - t_last.month)*30 + (t.year - t_last.year)*356
                    if(last_span > 0):
                        day_num += 1
                        day_interval.append(last_span)
                t_last = t

                log_list.append(t)

            #平均间隔
            interval_mean = np.array(day_interval).mean() if day_interval else 0

            #self.UCFeature.append([enrollment, log_num] + source_sts+event_sts+[day_num, span, interval_mean])
            self.user_course[enrollment] = [log_num] + source_sts+event_sts + \
                                           [day_num, span, interval_mean]
            self.log_time[enrollment] = log_list
