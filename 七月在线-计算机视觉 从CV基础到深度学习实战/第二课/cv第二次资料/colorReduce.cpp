// colorReduce.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


void colorReduce(cv::Mat& image, int div = 64)
{
	int nl = image.rows;                    // number of lines
	int nc = image.cols * image.channels(); // number of elements per line

	for (int j = 0; j < nl; j++)
	{
		// get the address of row j
		uchar* data = image.ptr<uchar>(j);

		for (int i = 0; i < nc; i++)
		{
			// process each pixel
			data[i] = data[i] / div * div;
		}
	}
}
void keamsCplus(cv::Mat& input, cv::Mat& output, int clusterCount = 4){
	cv::Mat src;
	input.copyTo(src);
	//step 1 : map the src to the samples
	cv::Mat samples = src.reshape(1, src.total());
	samples.convertTo(samples, CV_32F);
	//step 2 : apply kmeans to find labels and centers
	cv::Mat labels;
	int attempts = 5;//try 5 times, choose the best result
	cv::Mat centers;
	cv::kmeans(samples, clusterCount, labels,
		cv::TermCriteria(CV_TERMCRIT_ITER | CV_TERMCRIT_EPS,
		10, 0.01),
		attempts, cv::KMEANS_PP_CENTERS, centers);

	//step 3 : map the centers to the output
	// Now convert back into uint8, and make original image
	cv::Mat new_image(src.size(), src.type());
	cv::Mat red_samples(src.total(), 3, CV_8U);
	centers.convertTo(centers, CV_8U);
	for (int i = 0; i < src.total(); i++)
	{
		int clusterIdx = labels.at<int>(i);
		centers.row(clusterIdx).copyTo(red_samples.row(i));
	}
	new_image = red_samples.reshape(3, src.rows);
	new_image.copyTo(output);
}

int main(int argc, char* argv[])
{
	// Load input image (colored, 3-channel, BGR)
	cv::Mat input = cv::imread("boldt.jpg");
	if (input.empty())
	{
		std::cout << "!!! Failed imread()" << std::endl;
		return -1;
	}

	int divideWith = 64;
	uchar table[256];
	for (int i = 0; i < 256; ++i)
		table[i] = (uchar)(divideWith * (i / divideWith));
	cv::Mat lookUpTable(1, 256, CV_8U);
	uchar*p = lookUpTable.data;
	for (int i = 0; i < 256; i++)
		p[i] = table[i];
	cv::Mat result;
	LUT(input, lookUpTable, result);
	///////////////////
	//kmeans
	cv::Mat resultKmeans;
	keamsCplus(input, resultKmeans,8);
	//////////////////////
	colorReduce(input);
	///////////////////////
	cv::imshow("Color Reduction", input);
	cv::imwrite("output.jpg", input);
	cv::waitKey(0);

	return 0;
}