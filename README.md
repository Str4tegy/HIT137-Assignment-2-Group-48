/////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////
//   _______   _______        __        ________      _          _   _______   //
//  |  ___  | |  _____|      /  \      |  ____  \    | \        / | |  _____|  //
//  | |   | | | |_____      / /\ \     | |    \  |   |  \      /  | | |_____   //
//  | |___| | |  _____|    / /__\ \    | |     | |   | \ \    / / | |  _____|  //
//  |    __/  | |         / ______ \   | |     | |   | |\ \  / /| | | |        //
//  | |\ \    | |_____   / /      \ \  | |____/  |   | | \ \/ / | | | |_____   //
//  |_| \_\   |_______| /_/        \_\ |________/    |_|  \__/  |_| |_______|  //
//                                                                             //
/////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

//---------------------------//  THIS REPOSITORY  //---------------------------//

This repository contains 3 short python scripts which perform unrelated tasks.
The purpose of these scripts is to demonstrate various python concepts in various applications.

//--------------------------//  ENCRYPTION SCRIPT  //--------------------------//
                                  (Question One)

The function of this script is to encript and decrypt text.
This is accomplished through several sub-functions within the script.
First, the user inputs two values which are used as the encryption key to encrypt the file "raw_text.txt", given this file is in the same folder as the script.
The encrypted text which results from this are written into a file called "encrypted_text.txt" (which is stored in the same folder as the script).
The encryption key is then used to decrypt the text, and the text which results from the decryption process is written into a file called "decrypted_text.txt" (which is stored in the same folder as the script).
Finally, the program compares the text in the "raw_text.txt" and "decrypted_text.txt" files to ensure they match, to verify that the file was sucessfully decrypted.


//------------------------//  WEATHER DATA ANALYSIS  //------------------------//
                                  (Question Two)

The function of this script is to analyse the data from a set of CSV files and to provide an alysis of this weather data.
This script reads the CSV files it is in the same folder as to collect all required weather data from the various weather stations.
The script then utilises this data to determine the average temperature for each season, for each year, at each weather station, which is written in a file called "average_temp.txt" (which is stored in the same folder as the script).
Next, the ten stations with the highest range in temperature are determined and written in a file called "largest_temp_range_station.txt" (which is stored in the sam folder as the script).
Finally, the station with the most stable temperature and least stable temperature (based on standard deviation values) are determined, as well as any stations with equal standard deviation values. These values are written in a file called "temperature_stability_stations.txt" (which is stored in the same folder as the script).

                                                                                 
//----------------------//  RECURSIVE GEOMETRY SHAPES  //----------------------//
                                 (Question Three)

The function of this script is t create fractal polygons utilisn Python's turtle graphics.
The user first inputs the number of sides, the side length, and the recursion depth of their desired fractal polygon.
Based on these values, the script replaces each straight edge of a polygon with four smaller segments to form an inward pointing indentation.
Next, the script applies this process to every side of the shape and draws it in the turtle graphics.
The user is asked to enter the number of sides, the side length, and the recursion depth, and the program generates the fractal pattern on the screen.


