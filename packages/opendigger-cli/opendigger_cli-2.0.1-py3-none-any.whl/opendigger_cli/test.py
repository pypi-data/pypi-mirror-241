from fuzzywuzzy import process

# 候选列表
choices = ['openrank', 'activity', 'attention', 'active_dates_and_times',
                            'stars', 'technical_fork', 'participants', 'new_contributors',
                            'new_contributors_detail', 'inactive_contributors', 'bus_factor',
                            'bus_factor_detail', 'issues_new', 'issues_closed', 'issue_comments',
                            'issue_response_time', 'issue_resolution_duration', 'issue_age',
                            'code_change_lines_add', 'code_change_lines_remove',
                            'code_change_lines_sum', 'change_requests', 'change_requests_accepted',
                            'change_requests_reviews', 'change_request_response_time',
                            'change_request_resolution_duration', 'change_request_age',
                            'activity_details', 'developer_network', 'repo_network', 'project_openrank_detail']

# 输入
user_input = 'OPENNK'

# 进行模糊匹配
result = process.extractOne(user_input, choices)

# 输出匹配结果
print(f"匹配项: {result[0]}，相似度: {result[1]}")
print(result[1] == 100)