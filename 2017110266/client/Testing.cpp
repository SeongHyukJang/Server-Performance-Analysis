//#CURL_STATICLIB
#include <iostream>
//#include <curl/curl.h>

enum {
	ERROR_ARGS = 1 ,
	ERROR_CURL_INIT = 2
} ;

enum {
	OPTION_FALSE = 0 ,
	OPTION_TRUE = 1
} ;

enum {
	FLAG_DEFAULT = 0 
} ;

int main(const int argc,const char* argv[])
{
	if( argc != 2 ){
		std::cerr << " Usage: ./" << argv[0] << " {url} [debug]" << std::endl ;
		return( ERROR_ARGS ) ;
	}

	const char* url  = argv[1];

	// libcURL 초기화
	curl_global_init(CURL_GLOBAL_ALL);

	// context 객체 생성
	CURL *ctx = curl_easy_init();

	// context 객체 설정
	curl_easy_setopt(ctx, CURLOPT_URL, url);

	// no progress bar
	curl_easy_setopt(ctx, CURLOPT_NOPROGRESS, OPTION_TRUE);

	// 추가 설정 해주기
	// 헤더는 표준에러로 출력
	curl_easy_setopt(ctx, CURLOPT_WRITEHEADER, stderr);

	// body 데이터는 표준출력
	curl_easy_setopt(ctx, CURLOPT_WRITEDATA, stdout);


	///////// context 객체의 설정 종료 ////////////


	///////// 웹페이지 긁어오기 ////////////////////

	// curl_easy_perform을 이용하여 실제 페이지에를 긁어오기
	const CURLcode rc = curl_easy_perform(ctx);
	if(CURLE_OK != rc)
	{
		std::cerr << "Error from cURL: " << curl_easy_strerror(rc) << std::endl;
	}
	else
	{
		// get some info about the xfer
		double statDouble;
		long statLong;
		char* statString = NULL;

		// HTTP status code
		if(CURLE_OK == curl_easy_getinfo(ctx, CURLINFO_HTTP_CODE, &statLong))
		{
			std::cout << "Response code : " << statLong << std::endl;
		}

		// Content_type 얻어오기
		if(CURLE_OK == curl_easy_getinfo(ctx, CURLINFO_CONTENT_TYPE, &statString))
		{
			std::cout << "Content type : " << statString << std::endl;
		}

		if(CURLE_OK == curl_easy_getinfo(ctx, CURLINFO_SPEED_DOWNLOAD, &statDouble))
		{
			std::cout << "Download speed : " << statDouble << "bytes/sec" << std::endl;
		}
	}

	// cleanup
	curl_easy_cleanup(ctx);
	curl_global_cleanup();

	return 0;
}
