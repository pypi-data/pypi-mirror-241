# import time
# from tketool.ml.graph import graph
# from tketool.markdowns.markdown import draw_markdownobj
# from git import Repo
#
#
# class draw_gitbranches_graph(draw_markdownobj):
#     def __init__(self, git_repo_path):
#         self.repo_path = git_repo_path
#
#         self.repo = Repo(self.repo_path)
#
#     def str_out(self) -> [str]:
#         # 从远程仓库获取最新信息
#         self.repo.remotes.origin.fetch()
#         remote_branches = self.repo.remotes.origin.refs
#         all_branches = {}
#         grp = graph()
#         for branch in remote_branches:
#
#             # 获取该远程分支的所有提交
#             commits = list(self.repo.iter_commits(branch))
#             if len(commits) == 0:
#                 continue
#
#             all_commit_results = []
#             for commit in commits:
#                 for base_commit in commit.parents:
#                     all_commit_results.append((base_commit.hexsha, commit.hexsha, commit.committed_datetime))
#                 if len(commit.parents) == 0:
#                     all_commit_results.append(("", commit.hexsha, commit.committed_datetime))
#
#             all_branches[branch.name] = all_commit_results
#             # print(f'Remote branch: {branch.remote_head}')
#             # all_branches[branch.name] = [(commit.parents[0].hexsha if len(commit.parents) > 0 else "",
#             #                               commit.hexsha,
#             #                               commit.committed_datetime) for
#             #                              commit in commits]
#
#             for cp, cc, time in all_branches[branch.name]:
#                 if cp not in grp:
#                     grp.add_node(cp)
#                 if cc not in grp:
#                     grp.add_node(cc)
#                 grp.add_line(cp, cc, (branch.name, time))
#
#         # 减法去除引用提交
#
#         len_count_list_keys = sorted(all_branches.keys(), key=lambda x: len(all_branches[x]))
#         filter_connect_set = set()
#         for key in len_count_list_keys:
#             for commit in all_branches[key]:
#                 filter_key = commit[0] + "__" + commit[1]
#                 if filter_key in filter_connect_set:
#                     continue
#                 else:
#                     grp[commit[1]] = key
#                     filter_connect_set.add(filter_key)
#
#
#         branch_action_dic = {}
#         for br, br_list in all_branches.items():
#             first_item = br_list[0]
#             last_item = None
#             check_out_brance = None
#             for cm in br_list[1:]:
#                 node_branch, commit_time = grp[cm[1]]
#                 if node_branch != br:
#                     check_out_brance = node_branch
#                     break
#                 else:
#                     last_item = (node_branch, commit_time)
#
#             branch_action_dic[br] = (first_item, last_item, check_out_brance)
#
#         return ""
#
#
# dgg = draw_gitbranches_graph("/Users/kejiang/Code/test_git")
#
# dgg_out = dgg.str_out()
# time.time()
