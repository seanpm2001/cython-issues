# encoding: utf-8
# cython: profile=False

def show():
    a_str=b"""\x31\x39\x37\x36\xe5\xb9\xb4\x39\xe6\x9c\x88\x39\xe6\x97\xa5\xef\xbc\x8c\xe5\x9c\xa8\xe6\xaf\x9b\xe6\xb3\xbd\xe4\xb8\x9c\xe9\x80\x9d\xe4\xb8\x96\xe4\xb9\x8b\xe5\x90\x8e\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe5\xbc\x80\xe5\xa7\x8b\xe7\x94\xb1\xe8\x87\xaa\xe7\x94\xb1\xe5\x8c\x96\xe7\x9f\xa5\xe8\xaf\x86\xe5\x88\x86\xe5\xad\x90\xe3\x80\x81\xe9\xa2\x86\xe5\xaf\xbc\xe9\x98\xb6\xe5\xb1\x82\xe7\x9a\x84\xe5\x85\xb7\xe6\x9c\x89\xe6\x94\xb9\xe9\x9d\xa9\xe6\x80\x9d\xe6\x83\xb3\xe7\x9a\x84\xe4\xba\xba\xe5\xa3\xab\xe5\x92\x8c\xe5\xb9\xbf\xe5\xa4\xa7\xe6\xb0\x91\xe9\x97\xb4\xe5\x85\xb1\xe5\x90\x8c\xe8\xbf\x9b\xe8\xa1\x8c\xe7\x9a\x84\xe2\x80\x9c\xe6\x80\x9d\xe6\x83\xb3\xe8\xa7\xa3\xe6\x94\xbe\xe2\x80\x9d\xe8\xbf\x90\xe5\x8a\xa8\xe3\x80\x82\x31\x39\x37\x38\xe5\xb9\xb4\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe5\x85\xb1\xe4\xba\xa7\xe5\x85\x9a\xe5\x8d\x81\xe4\xb8\x80\xe5\xb1\x8a\xe4\xb8\x89\xe4\xb8\xad\xe5\x85\xa8\xe4\xbc\x9a\xe6\x8f\x90\xe5\x87\xba\xe6\x94\xb9\xe9\x9d\xa9\xe5\xbc\x80\xe6\x94\xbe\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe5\x9b\xbd\xe7\xad\x96\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba\xe6\xb0\x91\xe5\xaf\xb9\xe5\x85\xb6\xe6\x9c\x89\xe8\x8e\xab\xe5\xa4\xa7\xe7\x9a\x84\xe6\x86\xa7\xe6\x86\xac\xef\xbc\x8c\xe5\xb8\x8c\xe6\x9c\x9b\xe6\x91\x86\xe8\x84\xb1\xe5\x8d\x81\xe5\xb9\xb4\xe6\x96\x87\xe9\x9d\xa9\xe7\x9a\x84\xe6\xb7\xb7\xe4\xb9\xb1\xe5\x8f\x8a\xe8\xbf\x87\xe5\x8e\xbb\xe7\x9a\x84\xe8\xb4\xab\xe7\xa9\xb7\xe3\x80\x82\x31\x39\x38\x35\xe5\xb9\xb4\xef\xbc\x8c\xe6\x94\xbf\xe5\xba\x9c\xe6\x89\xa9\xe5\xa4\xa7\xe4\xba\x86\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9a\x84\xe8\x87\xaa\xe4\xb8\xbb\xe6\x9d\x83\xef\xbc\x8c\xe9\x81\xa3\xe8\xbf\x94\xe7\xa7\x81\xe8\x90\xa5\xe4\xbc\x81\xe4\xb8\x9a\xe4\xb8\xad\xe7\x9a\x84\xe5\x85\xac\xe6\x96\xb9\xe4\xbb\xa3\xe8\xa1\xa8\xef\xbc\x8c\xe5\xbc\x95\xe5\x85\xa5\xe5\xb8\x82\xe5\x9c\xba\xe7\xbb\x8f\xe6\xb5\x8e\xe4\xb8\xad\xe7\x9a\x84\xe8\xae\xb8\xe5\xa4\x9a\xe8\xa7\x82\xe5\xbf\xb5\xef\xbc\x8c\xe5\x8f\x91\xe5\xb1\x95\xe4\xb8\xba\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe5\xb8\x82\xe5\x9c\xba\xe7\xbb\x8f\xe6\xb5\x8e\xef\xbc\x9b\xe4\xbd\x86\xe5\x90\x8c\xe6\x97\xb6\xe4\xba\xa6\xe5\x9c\xa8\xe5\x8e\x9f\xe6\x9c\x89\xe8\xae\xa1\xe5\x88\x92\xe7\xbb\x8f\xe6\xb5\x8e\xe7\x90\x86\xe8\xae\xba\xe9\x81\xad\xe5\x88\xb0\xe6\x8a\x9b\xe5\xbc\x83\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b\xe5\xbc\x95\xe5\x8f\x91\xe4\xba\x86\xe5\x9b\xbd\xe5\x86\x85\xe6\xb0\x91\xe4\xbc\x97\xe7\x9a\x84\xe6\x80\x9d\xe6\x83\xb3\xe6\xb7\xb7\xe4\xb9\xb1\xe3\x80\x82\xe5\x8f\x8a\xe5\x90\x8e\xe5\x90\x84\xe5\x9c\xb0\xe5\x9b\xbd\xe8\x90\xa5\xe4\xbc\x81\xe4\xb8\x9a\xe5\x85\xb3\xe9\x97\xad\xef\xbc\x8c\xe5\x85\xa8\xe5\x9b\xbd\xe7\xba\xa6\xe6\x9c\x89\xe6\x95\xb0\xe7\x99\xbe\xe4\xb8\x87\xe5\xb7\xa5\xe4\xba\xba\xe5\xa4\xb1\xe4\xb8\x9a\xef\xbc\x8c\xe5\x9c\xa8\xe5\xbd\x93\xe6\x97\xb6\xe4\xb8\xad\xe5\x9b\xbd\xe6\x94\xbf\xe5\xba\x9c\xe5\x8f\x97\xe5\x88\xb0\xe4\xba\x86\xe6\x9e\x81\xe5\xa4\xa7\xe5\x86\xb2\xe5\x87\xbb\xe3\x80\x82\xe5\x90\x8c\xe6\x97\xb6\xe4\xba\xa6\xe5\xbc\x95\xe5\x8f\x91\xe8\xb4\xaa\xe6\xb1\xa1\xe8\x85\x90\xe8\xb4\xa5\xe7\x89\xa9\xe4\xbb\xb7\xe5\x8d\x87\xe6\xb6\xa8\xe7\xad\x89\xe9\x97\xae\xe9\xa2\x98\xef\xbc\x8c\xe5\x9c\xa8\xe6\xb0\x91\xe9\x97\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xb8\x80\xe5\xae\x9a\xe7\x9a\x84\xe4\xb8\x8d\xe6\xbb\xa1\xe3\x80\x82\x5b\x31\x5d\x5b\x32\x5d\x32\x30\xe4\xb8\x96\xe7\xba\xaa\x38\x30\xe5\xb9\xb4\xe4\xbb\xa3\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xe6\xad\xa3\xe5\xa4\x84\xe4\xba\x8e\xe5\x86\xb7\xe6\x88\x98\xe7\x9a\x84\xe6\x9c\x80\xe5\x90\x8e\xe9\x98\xb6\xe6\xae\xb5\xe3\x80\x82\x31\x39\x38\x35\xe5\xb9\xb4\xef\xbc\x8c\xe8\x8b\x8f\xe5\x85\xb1\xe4\xb8\xad\xe5\xa4\xae\xe6\x80\xbb\xe4\xb9\xa6\xe8\xae\xb0\xe6\x88\x88\xe5\xb0\x94\xe5\xb7\xb4\xe4\xb9\x94\xe5\xa4\xab\xe4\xb8\x8a\xe5\x8f\xb0\xef\xbc\x8c\xe6\x8e\xa8\xe8\xa1\x8c\xe4\xbb\xa5\xe4\xba\xba\xe9\x81\x93\xe4\xb8\xbb\xe4\xb9\x89\xe4\xb8\xba\xe6\xa0\xb8\xe5\xbf\x83\xe7\x9a\x84\xe2\x80\x9c\xe6\x96\xb0\xe6\x80\x9d\xe7\xbb\xb4\xe2\x80\x9d\xe8\xbf\x90\xe5\x8a\xa8\xef\xbc\x8c\xe5\x9c\xa8\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe9\x98\xb5\xe8\x90\xa5\xe5\x86\x85\xe4\xba\xa7\xe7\x94\x9f\xe5\xb9\xbf\xe6\xb3\x9b\xe5\xbd\xb1\xe5\x93\x8d\xe3\x80\x82\xe8\xa2\xab\xe5\x8c\x97\xe4\xba\xac\xe6\x94\xbf\xe5\xba\x9c\xe7\xa7\xb0\xe2\x80\x9c\xe8\xb5\x84\xe4\xba\xa7\xe9\x98\xb6\xe7\xba\xa7\xe8\x87\xaa\xe7\x94\xb1\xe5\x8c\x96\xe2\x80\x9d\xe6\x80\x9d\xe6\x83\xb3\xe7\x9a\x84\xe8\xa5\xbf\xe6\x96\xb9\xe6\xb0\x91\xe4\xb8\xbb\xe6\x80\x9d\xe6\xbd\xae\xe4\xb9\x9f\xe5\x9c\xa8\xe4\xb8\xad\xe5\x9b\xbd\xe5\xbe\x97\xe5\x88\xb0\xe5\xb9\xbf\xe6\xb3\x9b\xe4\xbc\xa0\xe6\x92\xad\xe3\x80\x82\xe5\xbe\x88\xe5\xa4\x9a\xe4\xba\xba\xe8\xae\xa4\xe4\xb8\xba\xe9\x9a\x8f\xe7\x9d\x80\xe6\x94\xb9\xe9\x9d\xa9\xe5\xbc\x80\xe6\x94\xbe\xe4\xbb\xa5\xe5\x8f\x8a\xe5\xb8\x82\xe5\x9c\xba\xe7\xbb\x8f\xe6\xb5\x8e\xe7\x90\x86\xe5\xbf\xb5\xe7\x9a\x84\xe5\xbc\x95\xe5\x85\xa5\xef\xbc\x8c\xe5\xae\xa3\xe5\x91\x8a\xe4\xb8\xad\xe5\x9b\xbd\xe5\x85\xb1\xe4\xba\xa7\xe5\x85\x9a\xe8\x83\x8c\xe5\xbc\x83\xe4\xba\x86\xe9\xa9\xac\xe5\x88\x97\xe4\xb8\xbb\xe4\xb9\x89\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe4\xbf\xa1\xe6\x9d\xa1\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe5\xb7\xb2\xe4\xb8\x8d\xe5\x86\x8d\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe5\x9b\xbd\xe5\xae\xb6\xef\xbc\x8c\xe8\x80\x8c\xe6\x98\xaf\xe5\x85\xb7\xe6\x9c\x89\xe6\x9f\x90\xe7\xa7\x8d\xe8\xb5\x84\xe6\x9c\xac\xe4\xb8\xbb\xe4\xb9\x89\xe6\x80\xa7\xe8\xb4\xa8\xe7\x9a\x84\xe7\xa4\xbe\xe4\xbc\x9a\xe3\x80\x82\x31\x39\x38\x38\xe5\xb9\xb4\xef\xbc\x8c\xe5\x85\xac\xe5\xbc\x80\xe5\x91\xbc\xe5\x94\xa4\xe2\x80\x9c\xe8\x94\x9a\xe8\x93\x9d\xe8\x89\xb2\xe2\x80\x9d\xe8\xa5\xbf\xe6\x96\xb9\xe6\x96\x87\xe6\x98\x8e\xe7\x9a\x84\xe6\x94\xbf\xe8\xae\xba\xe7\x94\xb5\xe8\xa7\x86\xe7\x89\x87\xe3\x80\x8a\xe6\xb2\xb3\xe6\xae\x87\xe3\x80\x8b\xe5\x9c\xa8\xe4\xb8\xad\xe5\xa4\xae\xe7\x94\xb5\xe8\xa7\x86\xe5\x8f\xb0\xe5\x85\xac\xe5\xbc\x80\xe6\x92\xad\xe5\x87\xba\xef\xbc\x8c\xe5\x9c\xa8\xe5\x85\xa8\xe5\x9b\xbd\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xbc\x95\xe8\xb5\xb7\xe8\xbd\xb0\xe5\x8a\xa8\xef\xbc\x8c\xe6\x88\x90\xe4\xb8\xba\xe5\x85\xad\xe5\x9b\x9b\xe8\xbf\x90\xe5\x8a\xa8\xe7\x9a\x84\xe6\x80\x9d\xe6\x83\xb3\xe5\x89\x8d\xe5\xaf\xbc\xe3\x80\x82\xe9\x9a\x8f\xe7\x9d\x80\xe4\xb8\xad\xe5\x9b\xbd\xe7\x9a\x84\xe5\xbc\x80\xe6\x94\xbe\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba\xe5\xbc\x80\xe5\xa7\x8b\xe6\x9b\xb4\xe5\xa4\x9a\xe5\x9c\xb0\xe6\x8e\xa5\xe8\xa7\xa6\xe8\xa5\xbf\xe6\x96\xb9\xe6\xb0\x91\xe4\xb8\xbb\xe4\xba\xba\xe6\x9d\x83\xe6\x80\x9d\xe6\x83\xb3\xef\xbc\x8c\xe5\xbe\x88\xe5\xa4\x9a\xe7\x9f\xa5\xe8\xaf\x86\xe5\x88\x86\xe5\xad\x90\xe5\xbc\x80\xe5\xa7\x8b\xe5\x85\xac\xe5\xbc\x80\xe6\x8f\x90\xe5\x80\xa1\xe4\xba\xba\xe6\x9d\x83\xe4\xb8\x8e\xe6\xb0\x91\xe4\xb8\xbb\xef\xbc\x8c\xe8\xae\xb8\xe5\xa4\x9a\xe5\xad\xa6\xe7\x94\x9f\xe6\x9b\xb4\xe6\x98\xaf\xe9\x80\x9a\xe8\xbf\x87\xe5\x90\x84\xe7\xa7\x8d\xe5\xbd\xa2\xe5\xbc\x8f\xe8\xa1\xa8\xe8\xbe\xbe\xe8\xbf\x99\xe6\x96\xb9\xe9\x9d\xa2\xe7\x9a\x84\xe8\xaf\x89\xe6\xb1\x82\xe3\x80\x82\xe4\xbb\x8e\xe4\xb8\x96\xe7\x95\x8c\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe7\x9c\x8b\xef\xbc\x8c\xe5\x85\xad\xe5\x9b\x9b\xe8\xbf\x90\xe5\x8a\xa8\xe5\xb9\xb6\xe9\x9d\x9e\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe5\xad\xa4\xe7\xab\x8b\xe7\x9a\x84\xe4\xba\x8b\xe4\xbb\xb6\xef\xbc\x8c\xe8\x80\x8c\xe6\x98\xaf\xe5\xbd\x93\xe6\x97\xb6\xe6\x95\xb4\xe4\xb8\xaa\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe9\x98\xb5\xe8\x90\xa5\xe5\x86\x85\xe6\xb0\x91\xe4\xb8\xbb\xe8\xbf\x90\xe5\x8a\xa8\xe7\x9a\x84\xe4\xb8\x80\xe4\xb8\xaa\xe9\x87\x8d\xe8\xa6\x81\xe7\x8e\xaf\xe8\x8a\x82\xe3\x80\x82\xe5\x9c\xa8\xe5\x85\xad\xe5\x9b\x9b\xe4\xba\x8b\xe4\xbb\xb6\xe5\x8f\x91\xe7\x94\x9f\xe7\x9a\x84\xe5\x90\x8c\xe4\xb8\x80\xe5\xa4\xa9\xef\xbc\x8c\xe6\xb3\xa2\xe5\x85\xb0\xe5\x9b\xa2\xe7\xbb\x93\xe5\xb7\xa5\xe4\xbc\x9a\xe5\x9c\xa8\xe5\xa4\xa7\xe9\x80\x89\xe4\xb8\xad\xe8\x8e\xb7\xe8\x83\x9c\xef\xbc\x8c\xe6\x8e\xa8\xe7\xbf\xbb\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe5\x88\xb6\xe5\xba\xa6\xe3\x80\x82\xe9\x9a\x8f\xe5\x90\x8e\xe4\xb8\x8d\xe5\x88\xb0\xe4\xb8\x80\xe5\xb9\xb4\xef\xbc\x8c\xe4\xb8\x9c\xe6\xac\xa7\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe5\x9b\xbd\xe5\xae\xb6\xe4\xb9\x9f\xe5\x85\x88\xe5\x90\x8e\xe5\x8f\x91\xe7\x94\x9f\xe5\x92\x8c\xe5\xb9\xb3\xe6\xbc\x94\xe5\x8f\x98\xef\xbc\x8c\xe4\xb8\xa4\xe5\xb9\xb4\xe5\x90\x8e\xe8\x8b\x8f\xe8\x81\x94\xe4\xba\xa6\xe5\xae\xa3\xe5\x91\x8a\xe8\xa7\xa3\xe4\xbd\x93\xef\xbc\x8c\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe9\x98\xb5\xe8\x90\xa5\xe8\xa7\xa3\xe4\xbd\x93\xe3\x80\x82\xe8\xbf\x99\xe4\xba\x9b\xe5\xae\x9e\xe8\xa1\x8c\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xb8\xbb\xe4\xb9\x89\xe5\x88\xb6\xe5\xba\xa6\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xe5\x9c\xa8\xe4\xb8\x8d\xe5\x88\xb0\x35\xe5\xb9\xb4\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4\xe4\xb8\xad\xe5\x8f\x91\xe7\x94\x9f\xe4\xba\x86\xe6\x94\xbf\xe6\x9d\x83\xe8\xbd\xae\xe6\x9b\xbf\xef\xbc\x8c\xe5\xb9\xb6\xe6\x94\xb9\xe5\x8f\x98\xe4\xba\x86\xe5\x8e\x9f\xe6\x9c\x89\xe7\x9a\x84\xe6\x94\xbf\xe6\xb2\xbb\xe4\xbd\x93\xe5\x88\xb6\xe3\x80\x82\x31\x39\x38\x37\xe5\xb9\xb4\x31\xe6\x9c\x88\xef\xbc\x8c\xe5\x8e\x9f\xe6\x9c\xac\xe8\xa2\xab\xe9\x82\x93\xe5\xb0\x8f\xe5\xb9\xb3\xe9\x80\x89\xe5\xae\x9a\xe4\xb8\xba\xe6\x8e\xa5\xe7\x8f\xad\xe4\xba\xba\xe7\x9a\x84\xe8\x83\xa1\xe8\x80\x80\xe9\x82\xa6\xe8\xa2\xab\xe8\xbf\xab\xe4\xb8\x8b\xe5\x8f\xb0\xef\xbc\x8c\xe4\xbb\x96\xe8\xa2\xab\xe6\x8c\x87\xe8\xbf\x9d\xe5\x8f\x8d\xe4\xb8\xad\xe5\x9b\xbd\xe5\x85\xb1\xe4\xba\xa7\xe5\x85\x9a\xe7\x9a\x84\xe6\xb0\x91\xe4\xb8\xbb\xe9\x9b\x86\xe4\xb8\xad\xe5\x88\xb6\xef\xbc\x8c\xe7\xba\xb5\xe5\xae\xb9\xe8\xb5\x84\xe4\xba\xa7\xe9\x98\xb6\xe7\xba\xa7\xe8\x87\xaa\xe7\x94\xb1\xe5\x8c\x96\xef\xbc\x8c\xe6\xb2\xa1\xe6\x9c\x89\xe5\xaf\xb9\xe6\xb8\xb8\xe8\xa1\x8c\xe9\x87\x87\xe5\x8f\x96\xe6\x9c\x89\xe6\x95\x88\xe6\x8e\xaa\xe6\x96\xbd\xef\xbc\x8c\xe8\xa6\x81\xe5\xaf\xb9\x31\x39\x38\x36\xe5\xb9\xb4\xe5\xad\xa6\xe7\x94\x9f\xe8\xbf\x90\xe5\x8a\xa8\xe7\x9a\x84\xe5\xa4\xb1\xe6\x8e\xa7\xe8\xb4\x9f\xe8\xb4\xa3\xe3\x80\x82\xe5\x8f\x8a\xe5\x90\x8e\xe4\xb8\xad\xe5\x85\xb1\xe5\x85\x9a\xe5\x86\x85\xe5\x8f\x8d\xe6\x94\xb9\xe9\x9d\xa9\xe7\x9a\x84\xe2\x80\x9c\xe4\xbf\x9d\xe5\xae\x88\xe2\x80\x9d\xe5\x8a\xbf\xe5\x8a\x9b\xe6\x8e\x80\xe8\xb5\xb7\xe4\xb8\x80\xe8\x82\xa1\xe5\x8f\x8d\xe5\x8f\xb3\xe6\xb5\xaa\xe6\xbd\xae\xe3\x80\x82\x0a\x0a\xe6\xb3\x95\xe8\xbd\xae\xe5\x8a\x9f\xe5\x8f\x88\xe7\xa7\xb0\xe6\xb3\x95\xe8\xbd\xae\xe5\xa4\xa7\xe6\xb3\x95\xef\xbc\x8c\xe6\xb3\x95\xe8\xbd\xae\xe5\x8a\x9f\xe5\x8a\x9f\xe6\xb3\x95\xe6\x98\xaf\xe7\x94\xb1\xe4\xba\x94\xe5\xa5\x97\xe5\x8a\xa8\xe4\xbd\x9c\xe7\xbb\x84\xe6\x88\x90\xef\xbc\x8c\xe4\xbd\x86\xe4\xb8\x8d\xe5\x90\x8c\xe4\xba\x8e\xe4\xb8\x80\xe8\x88\xac\xe6\xb0\x94\xe5\x8a\x9f\xe7\x9a\x84\xe6\x98\xaf\xe7\x9d\x80\xe9\x87\x8d\xe5\xbf\x83\xe6\x80\xa7\xe7\x9a\x84\xe4\xbf\xae\xe7\x82\xbc\xef\xbc\x8c\xe5\x8d\xb3\xe2\x80\x9c\xe7\x9c\x9f\xe3\x80\x81\xe5\x96\x84\xe3\x80\x81\xe5\xbf\x8d\xe2\x80\x9d\xe7\x9a\x84\xe5\x8e\x9f\xe5\x88\x99\xe3\x80\x82\xe4\xb8\x80\xe4\xba\x9b\xe4\xba\xba\xe8\xae\xa4\xe4\xb8\xba\xe6\xb3\x95\xe8\xbd\xae\xe5\x8a\x9f\xe5\x80\x9f\xe7\x94\xa8\xe4\xba\x86\xe5\xbe\x88\xe5\xa4\x9a\xe4\xbd\x9b\xe6\x95\x99\xe8\xa7\x82\xe5\xbf\xb5\xef\xbc\x8c\xe5\xa6\x82\xe6\xb3\x95\xe8\xbd\xae\xe3\x80\x81\xe4\xb8\x9a\xe7\xad\x89\xef\xbc\x8c\xe5\x9b\xa0\xe8\x80\x8c\xe8\xa7\x86\xe4\xb9\x8b\xe4\xb8\xba\xe4\xb8\x80\xe7\xa7\x8d\xe5\xae\x97\xe6\x95\x99\xe3\x80\x82\xe4\xbd\x86\xe6\xb3\x95\xe8\xbd\xae\xe5\x8a\x9f\xe5\xad\xa6\xe5\x91\x98\xe8\xae\xa4\xe4\xb8\xba\xe2\x80\x9c\xe6\xb3\x95\xe8\xbd\xae\xe2\x80\x9d\xe5\x92\x8c\xe2\x80\x9c\xe4\xb8\x9a\xe2\x80\x9d\xe9\x83\xbd\xe4\xb8\x8d\xe6\x98\xaf\xe4\xbd\x9b\xe6\x95\x99\xe4\xb8\x93\xe7\x94\xa8\xe7\x9a\x84\xef\xbc\x8c\xe5\x85\xb6\xe4\xb8\xad\xe4\xb8\x9a\xe7\x9a\x84\xe6\xa6\x82\xe5\xbf\xb5\xe5\x9c\xa8\xe5\xa9\x86\xe7\xbd\x97\xe9\x97\xa8\xe6\x95\x99\xe6\x88\x96\xe6\x9b\xb4\xe6\x97\xa9\xe7\x9a\x84\xe4\xbf\xae\xe7\x82\xbc\xe6\x96\xb9\xe6\xb3\x95\xe5\x92\x8c\xe5\xae\x97\xe6\x95\x99\xe5\xb0\xb1\xe5\xb7\xb2\xe7\xbb\x8f\xe5\xad\x98\xe5\x9c\xa8\xe4\xba\x86\xe3\x80\x82\x0a\x0a\xe5\x8f\xb0\xe7\x8b\xac\xe5\x95\x8a\xe5\x8f\xb0\xe7\x8b\xac\xe4\xb8\x80\xe5\x8f\xb0\xe7\x8b\xac\xe7\xab\x8b\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\x0a\x0a"""
    print a_str.decode('utf8')

if '__main__' == __name__:
    show()