import csv

# Provided text data
text_data = '''date,pitch,mph,spin_rate,pitcher,batter,ev,la,distance,count,inning,pitch_result,pa_result
2022-10-04	FF	90.3	2360	Abbott, Cory(R)	Alonso, Pete(R)	96.3	52°	253	
0-0	Bot 4	Hit Into Play	
Pete Alonso pops out to second baseman Luis Garcia.

2022-10-04	FF	90.5	2207	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Ball	
Pete Alonso walks.

2022-10-04	FF	91.1	2309	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
3-1	Bot 3	Foul Tip	
Pete Alonso walks.

2022-10-04	FF	90.0	2150	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
2-1	Bot 3	Ball	
Pete Alonso walks.

2022-10-04	KC	82.2	2409	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso walks.

2022-10-04	FF	90.2	2168	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Called Strike	
Pete Alonso walks.

2022-10-04	FF	89.1	2094	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso walks.

2022-10-04	FC	90.4	2182	Garrett, Reed(R)	Alonso, Pete(R)	92.4	15°	232	
2-2	Bot 2	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FF	95.4	2278	Garrett, Reed(R)	Alonso, Pete(R)	70.3	56°	175	
2-2	Bot 2	Foul	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FF	95.2	2325	Garrett, Reed(R)	Alonso, Pete(R)	--	°		
1-2	Bot 2	Ball	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FF	94.4	2245	Garrett, Reed(R)	Alonso, Pete(R)	--	°		
0-2	Bot 2	Ball	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FC	88.4	2285	Garrett, Reed(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Called Strike	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FF	99.1	2208	Harvey, Hunter(R)	Alonso, Pete(R)	92.1	45°	255	
3-2	Bot 4	Hit Into Play	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	ST	77.2	2702	Espino, Paolo(R)	Alonso, Pete(R)	85.9	6°	95	
0-1	Bot 1	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Josh Palacios, deflected by shortstop CJ Abrams.

2022-10-04	FF	94.5	2246	Garrett, Reed(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Swinging Strike	
Pete Alonso singles on a line drive to left fielder Josh Palacios.

2022-10-04	FF	98.6	2245	Harvey, Hunter(R)	Alonso, Pete(R)	71.8	39°	233	
3-2	Bot 4	Foul	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	SL	85.5	2114	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
3-0	Bot 1	Blocked Ball	
Pete Alonso walks.

2022-10-04	ST	76.9	2681	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso singles on a ground ball to left fielder Josh Palacios, deflected by shortstop CJ Abrams.

2022-10-04	FF	89.9	2177	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso walks.

2022-10-04	FS	89.4	1176	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
2-2	Bot 4	Ball	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FF	89.7	2158	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso walks.

2022-10-04	FF	97.5	2061	Harvey, Hunter(R)	Alonso, Pete(R)	79.2	61°	193	
2-2	Bot 4	Foul	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FF	90.5	2181	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks.

2022-10-04	FF	97.3	2073	Harvey, Hunter(R)	Alonso, Pete(R)	65.0	52°	154	
2-2	Bot 4	Foul	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FF	98.0	2124	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
2-1	Bot 4	Called Strike	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FS	88.6	1121	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
1-1	Bot 4	Ball	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FF	98.5	2135	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Ball	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	FF	97.3	1998	Harvey, Hunter(R)	Alonso, Pete(R)	70.7	64°	138	
0-0	Bot 4	Foul	
Pete Alonso flies out to right fielder Lane Thomas.

2022-10-04	SL	87.5	1982	Machado, Andrés(R)	Alonso, Pete(R)	99.4	10°	192	
1-0	Bot 7	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Cesar Hernandez.

2022-10-04	SI	93.2	1899	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso singles on a line drive to left fielder Cesar Hernandez.

2022-10-02	FF	94.6	2311	Morton, Charlie(R)	Alonso, Pete(R)	96.1	28°	332	
0-1	Top 5	Hit Into Play	
Pete Alonso flies out to right fielder Ronald Acuna Jr.

2022-10-02	FF	93.8	2229	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso flies out to right fielder Ronald Acuna Jr.

2022-10-02	SI	95.0	1920	Morton, Charlie(R)	Alonso, Pete(R)	84.6	15°	232	
1-0	Top 3	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Eddie Rosario.

2022-10-02	CU	81.6	2973	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso singles on a line drive to left fielder Eddie Rosario.

2022-10-02	SI	95.8	2075	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
3-1	Top 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-10-02	CU	83.4	3094	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Blocked Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-10-02	SI	95.9	2200	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-0	Top 1	Called Strike	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-10-02	CU	82.4	3040	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-10-02	CU	82.4	3140	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-10-02	FF	94.0	2349	Iglesias, Raisel(R)	Alonso, Pete(R)	73.2	47°	222	
1-1	Top 7	Hit Into Play	
Pete Alonso pops out to second baseman Orlando Arcia.

2022-10-02	SI	93.3	2409	Iglesias, Raisel(R)	Alonso, Pete(R)	66.8	50°	169	
1-0	Top 7	Foul	
Pete Alonso pops out to second baseman Orlando Arcia.

2022-10-02	SI	93.0	2374	Iglesias, Raisel(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso pops out to second baseman Orlando Arcia.

2022-10-01	KC	85.6	2617	Wright, Kyle(R)	Alonso, Pete(R)	107.4	-3°	29	
0-2	Top 5	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Eddie Rosario.

2022-10-01	KC	86.3	2692	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Swinging Strike	
Pete Alonso singles on a ground ball to left fielder Eddie Rosario.

2022-10-01	SL	90.1	2363	Wright, Kyle(R)	Alonso, Pete(R)	--	°	8	
0-0	Top 5	Called Strike	
Pete Alonso singles on a ground ball to left fielder Eddie Rosario.

2022-10-01	SI	94.3	2276	Wright, Kyle(R)	Alonso, Pete(R)	89.3	-35°	3	
0-0	Top 3	Hit Into Play	
Pete Alonso grounds out, third baseman Austin Riley to first baseman Matt Olson.

2022-10-01	FC	89.4	2305	Chavez, Jesse(R)	Alonso, Pete(R)	93.0	35°	347	
0-1	Top 7	Hit Into Play	
Pete Alonso flies out to right fielder Ronald Acuna Jr.

2022-10-01	FC	88.6	2283	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso flies out to right fielder Ronald Acuna Jr.

2022-10-01	SI	96.0	2352	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
3-2	Top 1	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	SI	95.0	2366	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	KC	86.7	2745	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	SI	93.8	2215	Wright, Kyle(R)	Alonso, Pete(R)	69.9	-39°	3	
1-2	Top 1	Foul	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	KC	84.9	2710	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Called Strike	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	KC	85.6	2675	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Blocked Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-10-01	KC	85.4	2633	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Swinging Strike	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-30	SI	92.6	1984	Fried, Max(L)	Alonso, Pete(R)	87.1	33°	326	
0-0	Top 3	Hit Into Play	
Pete Alonso flies out to center fielder Michael Harris II.

2022-09-30	FF	96.3	2352	Minter, A.J.(L)	Alonso, Pete(R)	63.7	83°	41	
2-2	Top 8	Hit Into Play	
Pete Alonso pops out to catcher Travis d'Arnaud in foul territory.

2022-09-30	CH	86.9	1613	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
2-1	Top 8	Called Strike	
Pete Alonso pops out to catcher Travis d'Arnaud in foul territory.

2022-09-30	FF	96.2	2512	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso pops out to catcher Travis d'Arnaud in foul territory.

2022-09-30	FF	96.6	2430	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso pops out to catcher Travis d'Arnaud in foul territory.

2022-09-30	CH	88.2	1597	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso pops out to catcher Travis d'Arnaud in foul territory.

2022-09-30	SI	93.4	1997	Fried, Max(L)	Alonso, Pete(R)	94.8	16°	283	
0-1	Top 1	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Michael Harris II.

2022-09-30	FC	89.8	2705	McHugh, Collin(R)	Alonso, Pete(R)	99.9	-2°	31	
0-0	Top 6	Hit Into Play	
Pete Alonso grounds into a double play, second baseman Orlando Arcia to first baseman Matt Olson. Brandon Nimmo out at 2nd. Pete Alonso out at 1st.

2022-09-30	CU	73.2	2771	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso singles on a line drive to center fielder Michael Harris II.

2022-09-28	SI	95.0	2079	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Called Strike	
Pete Alonso called out on strikes.

2022-09-28	FF	95.6	2292	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Foul	
Pete Alonso called out on strikes.

2022-09-28	CH	86.9	1978	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso called out on strikes.

2022-09-28	CH	85.0	1933	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Swinging Strike	
Pete Alonso called out on strikes.

2022-09-28	SL	84.6	2485	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-09-28	FF	98.0	2297	Luzardo, Jesús(L)	Alonso, Pete(R)	72.1	43°	202	
2-2	Bot 3	Foul	
Pete Alonso strikes out on a foul tip.

2022-09-28	FF	97.8	2322	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso strikes out on a foul tip.

2022-09-28	FF	97.2	2278	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Swinging Strike	
Pete Alonso strikes out on a foul tip.

2022-09-28	CH	88.7	1901	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-09-28	FF	97.0	2319	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso strikes out on a foul tip.

2022-09-28	SL	86.3	2448	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-09-28	SL	86.6	2663	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
3-2	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	SL	88.8	2653	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	SI	95.9	2133	Luzardo, Jesús(L)	Alonso, Pete(R)	71.3	14°	135	
0-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-09-28	FF	95.9	2463	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Swinging Strike	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	SL	84.5	2231	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso strikes out swinging.

2022-09-28	SL	87.4	2592	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	FF	96.1	2449	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	FF	96.5	2529	Scott, Tanner(L)	Alonso, Pete(R)	68.8	55°	164	
0-0	Bot 8	Foul	
Pete Alonso walks. Brandon Nimmo to 2nd.

2022-09-28	ST	83.3	1480	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
3-2	Bot 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-28	FF	95.9	2372	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
2-2	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-09-28	FF	95.5	2426	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
2-1	Bot 9	Foul Tip	
Pete Alonso strikes out swinging.

2022-09-28	ST	81.3	2993	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
2-0	Bot 9	Called Strike	
Pete Alonso strikes out swinging.

2022-09-28	ST	81.8	2910	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-09-28	ST	81.2	2854	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-09-27	CU	81.7	2512	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-2	Bot 6	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-09-27	FF	94.8	2173	López, Pablo(R)	Alonso, Pete(R)	81.6	66°	148	
0-2	Bot 6	Foul	
Pete Alonso strikes out on a foul tip.

2022-09-27	CH	88.3	1994	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-09-27	FF	94.4	2365	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-09-27	CH	89.8	2037	López, Pablo(R)	Alonso, Pete(R)	100.3	33°	388	
3-2	Bot 4	Hit Into Play	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	SI	95.5	2050	López, Pablo(R)	Alonso, Pete(R)	77.6	7°	104	
3-1	Bot 4	Foul	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	CH	88.6	1999	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-1	Bot 4	Blocked Ball	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	FF	94.9	2316	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-1	Bot 4	Ball	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	CH	89.0	2048	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Foul	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	CH	88.4	2057	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso homers (40) on a fly ball to left center field. Brandon Nimmo scores. Francisco Lindor scores.

2022-09-27	SI	89.7	2019	Bleier, Richard(L)	Alonso, Pete(R)	74.2	-27°	3	
3-1	Bot 8	Hit Into Play	
Pete Alonso grounds out, second baseman Luke Williams to first baseman Lewin Diaz.

2022-09-27	SI	89.2	1944	Bleier, Richard(L)	Alonso, Pete(R)	--	°		
3-0	Bot 8	Called Strike	
Pete Alonso grounds out, second baseman Luke Williams to first baseman Lewin Diaz.

2022-09-27	FC	84.8	1919	Bleier, Richard(L)	Alonso, Pete(R)	--	°		
2-0	Bot 8	Ball	
Pete Alonso grounds out, second baseman Luke Williams to first baseman Lewin Diaz.

2022-09-27	SI	89.9	1987	Bleier, Richard(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso grounds out, second baseman Luke Williams to first baseman Lewin Diaz.

2022-09-27	SI	90.9	2000	Bleier, Richard(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso grounds out, second baseman Luke Williams to first baseman Lewin Diaz.

2022-09-27	SI	95.3	2074	López, Pablo(R)	Alonso, Pete(R)	91.2	28°	325	
2-1	Bot 2	Hit Into Play	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-27	CH	88.1	1961	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-1	Bot 2	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-27	CH	90.0	2122	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-27	FF	95.4	2267	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Called Strike	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-25	CH	81.9	1848	Sears, JP(L)	Alonso, Pete(R)	73.0	14°	119	
2-0	Top 3	Hit Into Play	
Pete Alonso lines out to first baseman Dermis Garcia.

2022-09-25	FF	92.6	2190	Sears, JP(L)	Alonso, Pete(R)	--	°		
1-0	Top 3	Ball	
Pete Alonso lines out to first baseman Dermis Garcia.

2022-09-25	CH	81.7	1873	Sears, JP(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso lines out to first baseman Dermis Garcia.

2022-09-25	CH	84.2	1666	Koenig, Jared(L)	Alonso, Pete(R)	101.6	24°	348	
2-1	Top 8	Hit Into Play	
Pete Alonso doubles (27) on a sharp fly ball to right fielder Conner Capel. Brandon Nimmo scores. Mark Canha scores. Francisco Lindor scores.

2022-09-25	SI	90.5	2254	Koenig, Jared(L)	Alonso, Pete(R)	--	°		
2-0	Top 8	Called Strike	
Pete Alonso doubles (27) on a sharp fly ball to right fielder Conner Capel. Brandon Nimmo scores. Mark Canha scores. Francisco Lindor scores.

2022-09-25	FC	82.0	2378	Koenig, Jared(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso doubles (27) on a sharp fly ball to right fielder Conner Capel. Brandon Nimmo scores. Mark Canha scores. Francisco Lindor scores.

2022-09-25	CU	78.7	2301	Koenig, Jared(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso doubles (27) on a sharp fly ball to right fielder Conner Capel. Brandon Nimmo scores. Mark Canha scores. Francisco Lindor scores.

2022-09-25	FF	92.1	2142	Sears, JP(L)	Alonso, Pete(R)	82.3	9°	121	
1-0	Top 2	Hit Into Play	
Pete Alonso singles on a ground ball to second baseman Jordan Diaz, deflected by shortstop Ernie Clement.

2022-09-25	FF	92.7	2107	Sears, JP(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso singles on a ground ball to second baseman Jordan Diaz, deflected by shortstop Ernie Clement.

2022-09-25	SI	91.0	2053	Selman, Sam(L)	Alonso, Pete(R)	72.8	50°	201	
0-1	Top 6	Hit Into Play	
Pete Alonso doubles (26) on a fly ball to right fielder Conner Capel.

2022-09-25	FF	89.9	2279	Selman, Sam(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso doubles (26) on a fly ball to right fielder Conner Capel.

2022-09-25	SL	88.0	2531	Ruiz, Norge(R)	Alonso, Pete(R)	110.6	26°	451	
2-2	Top 4	Hit Into Play	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-25	FF	94.3	2285	Ruiz, Norge(R)	Alonso, Pete(R)	78.0	10°	129	
2-2	Top 4	Foul	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-25	FF	93.5	2240	Ruiz, Norge(R)	Alonso, Pete(R)	60.9	35°	155	
2-1	Top 4	Foul	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-25	SL	85.5	2637	Ruiz, Norge(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-25	SL	85.5	2704	Ruiz, Norge(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Called Strike	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-25	FF	93.1	2247	Ruiz, Norge(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso homers (39) on a fly ball to left center field. Francisco Lindor scores.

2022-09-24	FF	93.5	2372	Waldichuk, Ken(L)	Alonso, Pete(R)	105.5	19°	355	
0-1	Top 3	Hit Into Play	
Pete Alonso lines out sharply to right fielder Conner Capel.

2022-09-24	ST	81.0	2087	Waldichuk, Ken(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso lines out sharply to right fielder Conner Capel.

2022-09-24	FF	94.4	2236	Waldichuk, Ken(L)	Alonso, Pete(R)	102.3	31°	410	
0-1	Top 1	Hit Into Play	
Pete Alonso homers (38) on a fly ball to left field. Mark Canha scores.

2022-09-24	FF	93.8	2304	Waldichuk, Ken(L)	Alonso, Pete(R)	71.5	75°	119	
0-0	Top 1	Foul	
Pete Alonso homers (38) on a fly ball to left field. Mark Canha scores.

2022-09-24	FF	97.7	2317	Puk, A.J.(L)	Alonso, Pete(R)	99.1	39°	328	
1-2	Top 8	Hit Into Play	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-24	FF	97.7	2351	Puk, A.J.(L)	Alonso, Pete(R)	--	°		
1-1	Top 8	Called Strike	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-24	SI	95.9	2401	Puk, A.J.(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Swinging Strike	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-24	SI	96.4	2476	Puk, A.J.(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-24	SL	86.2	2528	Pruitt, Austin(R)	Alonso, Pete(R)	82.2	58°	189	
0-1	Top 6	Hit Into Play	
Pete Alonso flies out to right fielder Conner Capel in foul territory.

2022-09-24	SL	87.0	2461	Pruitt, Austin(R)	Alonso, Pete(R)	72.1	8°	91	
0-0	Top 6	Foul	
Pete Alonso flies out to right fielder Conner Capel in foul territory.

2022-09-23	FC	86.8	2133	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
3-2	Top 9	Ball	
Pete Alonso walks.

2022-09-23	CU	76.9	2388	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
3-2	Top 9	Foul	
Pete Alonso walks.

2022-09-23	FF	90.5	1945	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Ball	
Pete Alonso walks.

2022-09-23	SL	79.3	2418	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso walks.

2022-09-23	FC	86.9	2141	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Foul Tip	
Pete Alonso walks.

2022-09-23	CH	84.5	1381	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso walks.

2022-09-23	SI	88.7	1975	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso walks.

2022-09-23	SI	90.2	2004	Irvin, Cole(L)	Alonso, Pete(R)	88.1	25°	314	
2-1	Top 3	Hit Into Play	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-23	FF	91.7	2081	Irvin, Cole(L)	Alonso, Pete(R)	--	°		
1-1	Top 3	Ball	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-23	FF	90.9	2031	Irvin, Cole(L)	Alonso, Pete(R)	--	°		
1-0	Top 3	Called Strike	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-23	FF	90.0	2077	Irvin, Cole(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso flies out to right fielder Conner Capel.

2022-09-23	CH	83.2	1548	Irvin, Cole(L)	Alonso, Pete(R)	84.3	4°	68	
1-0	Top 2	Hit Into Play	
Pete Alonso singles on a ground ball to center fielder Seth Brown.

2022-09-23	FF	89.1	1990	Irvin, Cole(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso singles on a ground ball to center fielder Seth Brown.

2022-09-23	FC	87.8	2309	Wiles, Collin(R)	Alonso, Pete(R)	63.3	-40°	3	
1-0	Top 7	Hit Into Play	
Pete Alonso grounds out, third baseman Vimael Machin to first baseman Dermis Garcia.

2022-09-23	FC	87.8	2312	Wiles, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso grounds out, third baseman Vimael Machin to first baseman Dermis Garcia.

2022-09-21	SL	87.5	2357	Houser, Adrian(R)	Alonso, Pete(R)	76.1	-22°	5	
3-2	Top 4	Hit Into Play	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	CU	83.8	2078	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
2-2	Top 4	Ball	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	FF	94.7	2123	Houser, Adrian(R)	Alonso, Pete(R)	76.1	17°	180	
2-2	Top 4	Foul	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	FF	93.2	2066	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Ball	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	FF	93.3	2072	Houser, Adrian(R)	Alonso, Pete(R)	81.4	54°	234	
1-1	Top 4	Foul	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	FF	93.3	2197	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	FF	92.1	2093	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso grounds out, shortstop Willy Adames to first baseman Rowdy Tellez.

2022-09-21	SI	92.9	2072	Houser, Adrian(R)	Alonso, Pete(R)	62.6	78°	48	
1-0	Top 1	Hit Into Play	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-09-21	SL	84.9	2217	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-09-21	FF	85.7	2135	Suter, Brent(L)	Alonso, Pete(R)	62.1	2°	41	
0-1	Top 8	Hit Into Play	
Pete Alonso grounds out, pitcher Brent Suter to first baseman Mike Brosseau.

2022-09-21	FF	87.5	2204	Suter, Brent(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso grounds out, pitcher Brent Suter to first baseman Mike Brosseau.

2022-09-21	SI	95.8	2093	Gott, Trevor(R)	Alonso, Pete(R)	87.9	-18°	4	
1-0	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Jace Peterson to first baseman Rowdy Tellez.

2022-09-21	FF	96.0	2225	Gott, Trevor(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out, third baseman Jace Peterson to first baseman Rowdy Tellez.

2022-09-20	ST	79.1	2727	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
1-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-20	ST	79.1	2699	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
1-1	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-09-20	SL	84.7	2604	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-20	SI	93.2	2216	Rogers, Taylor(L)	Alonso, Pete(R)	80.8	73°	139	
1-0	Top 7	Foul	
Pete Alonso strikes out swinging.

2022-09-20	SL	85.4	2474	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
2-1	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-09-20	ST	79.6	2737	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-09-20	SI	96.7	2343	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-09-20	SI	96.7	2253	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
1-0	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-09-20	SL	83.6	2575	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-09-20	FF	92.3	2337	Strzelecki, Peter(R)	Alonso, Pete(R)	105.1	-23°	5	
0-2	Top 4	Hit Into Play	
Pete Alonso grounds out sharply, second baseman Kolten Wong to first baseman Rowdy Tellez.

2022-09-20	FF	92.3	2365	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Called Strike	
Pete Alonso grounds out sharply, second baseman Kolten Wong to first baseman Rowdy Tellez.

2022-09-20	SL	83.1	2975	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso grounds out sharply, second baseman Kolten Wong to first baseman Rowdy Tellez.

2022-09-20	SL	86.9	2408	Boxberger, Brad(R)	Alonso, Pete(R)	108.3	23°	425	
1-1	Top 6	Hit Into Play	
Pete Alonso homers (37) on a fly ball to center field. Mark Canha scores. Francisco Lindor scores.

2022-09-20	FF	92.9	2416	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso homers (37) on a fly ball to center field. Mark Canha scores. Francisco Lindor scores.

2022-09-20	FF	93.1	2489	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso homers (37) on a fly ball to center field. Mark Canha scores. Francisco Lindor scores.

2022-09-19	FC	96.6	2689	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
3-2	Top 6	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-09-19	FC	96.6	2688	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
2-2	Top 6	Ball	
Pete Alonso strikes out on a foul tip.

2022-09-19	FC	94.5	2632	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
2-1	Top 6	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-09-19	FC	96.2	2676	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Ball	
Pete Alonso strikes out on a foul tip.

2022-09-19	FC	94.6	2434	Burnes, Corbin(R)	Alonso, Pete(R)	79.1	63°	193	
1-0	Top 6	Foul	
Pete Alonso strikes out on a foul tip.

2022-09-19	SL	88.7	2858	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Blocked Ball	
Pete Alonso strikes out on a foul tip.

2022-09-19	CH	90.6	1902	Burnes, Corbin(R)	Alonso, Pete(R)	113.1	27°	437	
1-2	Top 4	Hit Into Play	
Pete Alonso homers (36) on a fly ball to left field. Francisco Lindor scores. Jeff McNeil scores.

2022-09-19	CU	80.3	2797	Burnes, Corbin(R)	Alonso, Pete(R)	97.0	38°	336	
1-2	Top 4	Foul	
Pete Alonso homers (36) on a fly ball to left field. Francisco Lindor scores. Jeff McNeil scores.

2022-09-19	CU	82.2	2872	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Swinging Strike	
Pete Alonso homers (36) on a fly ball to left field. Francisco Lindor scores. Jeff McNeil scores.

2022-09-19	FC	96.2	2698	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso homers (36) on a fly ball to left field. Francisco Lindor scores. Jeff McNeil scores.

2022-09-19	FC	95.3	2523	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Foul	
Pete Alonso homers (36) on a fly ball to left field. Francisco Lindor scores. Jeff McNeil scores.

2022-09-19	SI	97.7	2555	Burnes, Corbin(R)	Alonso, Pete(R)	88.9	39°	309	
1-1	Top 2	Hit Into Play	
Pete Alonso flies out to center fielder Garrett Mitchell.

2022-09-19	SL	90.3	2918	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-1	Top 2	Ball	
Pete Alonso flies out to center fielder Garrett Mitchell.

2022-09-19	FC	96.1	2737	Burnes, Corbin(R)	Alonso, Pete(R)	64.5	-18°	7	
0-0	Top 2	Foul	
Pete Alonso flies out to center fielder Garrett Mitchell.

2022-09-19	FF	94.0	2475	Strzelecki, Peter(R)	Alonso, Pete(R)	73.4	46°	215	
2-2	Top 9	Hit Into Play	
Pete Alonso flies out to right fielder Hunter Renfroe.

2022-09-19	SL	82.4	3034	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso flies out to right fielder Hunter Renfroe.

2022-09-19	SL	82.9	3043	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Called Strike	
Pete Alonso flies out to right fielder Hunter Renfroe.

2022-09-19	FF	92.9	2392	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso flies out to right fielder Hunter Renfroe.

2022-09-19	SL	84.5	2962	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso flies out to right fielder Hunter Renfroe.

2022-09-19	SI	95.4	2101	Topa, Justin(R)	Alonso, Pete(R)	--	°		
3-2	Top 8	Ball	
Pete Alonso walks.

2022-09-19	SI	95.5	2093	Topa, Justin(R)	Alonso, Pete(R)	77.9	-25°	5	
3-1	Top 8	Foul	
Pete Alonso walks.

2022-09-19	SI	94.0	2046	Topa, Justin(R)	Alonso, Pete(R)	--	°		
3-0	Top 8	Called Strike	
Pete Alonso walks.

2022-09-19	SI	94.3	2063	Topa, Justin(R)	Alonso, Pete(R)	--	°		
2-0	Top 8	Ball	
Pete Alonso walks.

2022-09-19	SL	79.8	2534	Topa, Justin(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso walks.

2022-09-19	SI	95.4	2071	Topa, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso walks.

2022-09-18	SL	85.3	2690	Oviedo, Johan(R)	Alonso, Pete(R)	102.1	-10°	11	
0-2	Bot 4	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Oneil Cruz to second baseman Rodolfo Castro. Jeff McNeil out at 2nd.

2022-09-18	SL	84.5	2947	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Swinging Strike	
Pete Alonso grounds into a force out, shortstop Oneil Cruz to second baseman Rodolfo Castro. Jeff McNeil out at 2nd.

2022-09-18	FF	95.8	2220	Oviedo, Johan(R)	Alonso, Pete(R)	89.1	39°	266	
0-0	Bot 4	Foul	
Pete Alonso grounds into a force out, shortstop Oneil Cruz to second baseman Rodolfo Castro. Jeff McNeil out at 2nd.

2022-09-18	SL	87.1	2524	Oviedo, Johan(R)	Alonso, Pete(R)	75.9	11°	129	
0-0	Bot 2	Hit Into Play	
Pete Alonso grounds into a force out, second baseman Rodolfo Castro to shortstop Oneil Cruz. Tomas Nido scores. Brandon Nimmo to 3rd. Jeff McNeil out at 2nd. Pete Alonso to 1st.

2022-09-18	SL	88.6	2757	Crowe, Wil(R)	Alonso, Pete(R)	84.6	45°	243	
0-0	Bot 6	Hit Into Play	
Pete Alonso flies out to right fielder Cal Mitchell.

2022-09-18	FF	95.7	2163	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Hit By Pitch	
Pete Alonso hit by pitch. Jeff McNeil to 2nd.

2022-09-18	CU	84.0	2287	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
3-2	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-18	FF	93.4	2116	Underwood Jr., Duane(R)	Alonso, Pete(R)	71.2	23°	188	
3-1	Bot 8	Foul	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-18	FF	94.8	2172	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-18	SI	95.3	2116	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-18	FF	95.4	2085	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Swinging Strike	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-18	FF	94.0	2059	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso walks. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-17	SI	91.6	1816	Wilson, Bryse(R)	Alonso, Pete(R)	76.0	-1°	31	
0-1	Bot 5	Hit Into Play	
Pete Alonso grounds out, second baseman Rodolfo Castro to first baseman Michael Chavis.

2022-09-17	FF	92.9	1793	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso grounds out, second baseman Rodolfo Castro to first baseman Michael Chavis.

2022-09-17	CU	78.5	2248	Wilson, Bryse(R)	Alonso, Pete(R)	72.3	-23°	4	
2-2	Bot 3	Hit Into Play	
Pete Alonso grounds out, shortstop Oneil Cruz to first baseman Michael Chavis.

2022-09-17	FF	91.8	2395	De Jong, Chase(R)	Alonso, Pete(R)	--	°		
3-0	Bot 8	Ball	
Pete Alonso walks. Eduardo Escobar scores. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-17	FF	93.5	2026	Wilson, Bryse(R)	Alonso, Pete(R)	73.2	60°	170	
2-1	Bot 3	Foul	
Pete Alonso grounds out, shortstop Oneil Cruz to first baseman Michael Chavis.

2022-09-17	SL	84.4	2485	De Jong, Chase(R)	Alonso, Pete(R)	--	°		
2-0	Bot 8	Ball	
Pete Alonso walks. Eduardo Escobar scores. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-17	FF	93.0	2068	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
2-0	Bot 3	Called Strike	
Pete Alonso grounds out, shortstop Oneil Cruz to first baseman Michael Chavis.

2022-09-17	SL	81.3	2137	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Ball	
Pete Alonso grounds out, shortstop Oneil Cruz to first baseman Michael Chavis.

2022-09-17	SL	83.9	2512	De Jong, Chase(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso walks. Eduardo Escobar scores. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-17	CU	79.1	2411	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso grounds out, shortstop Oneil Cruz to first baseman Michael Chavis.

2022-09-17	FF	91.7	2388	De Jong, Chase(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso walks. Eduardo Escobar scores. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-17	SI	90.5	1889	Wilson, Bryse(R)	Alonso, Pete(R)	53.3	27°	133	
0-0	Bot 2	Hit Into Play	
Pete Alonso doubles (25) on a soft line drive to right fielder Ben Gamel.

2022-09-17	SL	84.0	2379	De Jong, Chase(R)	Alonso, Pete(R)	51.8	-28°	2	
0-2	Bot 7	Hit Into Play	
Pete Alonso grounds out softly to first baseman Michael Chavis. Jeff McNeil to 2nd.

2022-09-17	FF	92.6	2286	De Jong, Chase(R)	Alonso, Pete(R)	77.5	81°	99	
0-1	Bot 7	Foul	
Pete Alonso grounds out softly to first baseman Michael Chavis. Jeff McNeil to 2nd.

2022-09-17	SL	82.8	2324	De Jong, Chase(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso grounds out softly to first baseman Michael Chavis. Jeff McNeil to 2nd.

2022-09-16	ST	83.7	2770	Keller, Mitch(R)	Alonso, Pete(R)	98.7	47°	287	
2-0	Bot 6	Hit Into Play	
Pete Alonso out on a sacrifice fly to center fielder Bryan Reynolds. Brandon Nimmo scores.

2022-09-16	ST	84.7	2783	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Ball	
Pete Alonso out on a sacrifice fly to center fielder Bryan Reynolds. Brandon Nimmo scores.

2022-09-16	ST	85.1	2774	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso out on a sacrifice fly to center fielder Bryan Reynolds. Brandon Nimmo scores.

2022-09-16	SI	94.5	2219	Keller, Mitch(R)	Alonso, Pete(R)	93.7	17°	273	
1-0	Bot 4	Hit Into Play	
Pete Alonso lines out to right fielder Ben Gamel.

2022-09-16	ST	83.1	2750	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso lines out to right fielder Ben Gamel.

2022-09-16	ST	83.9	2778	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
1-2	Bot 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-16	FF	96.2	2480	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-2	Bot 2	Ball	
Pete Alonso strikes out swinging.

2022-09-16	FF	95.3	2395	Keller, Mitch(R)	Alonso, Pete(R)	79.6	20°	212	
0-2	Bot 2	Foul	
Pete Alonso strikes out swinging.

2022-09-16	FF	94.3	2410	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Called Strike	
Pete Alonso strikes out swinging.

2022-09-16	SI	94.4	2259	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Called Strike	
Pete Alonso strikes out swinging.

2022-09-16	FC	95.0	2146	Underwood Jr., Duane(R)	Alonso, Pete(R)	75.7	-22°	3	
1-1	Bot 8	Hit Into Play	
Pete Alonso grounds out, second baseman Rodolfo Castro to first baseman Michael Chavis.

2022-09-16	FC	92.1	2044	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Called Strike	
Pete Alonso grounds out, second baseman Rodolfo Castro to first baseman Michael Chavis.

2022-09-16	SI	96.5	2055	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso grounds out, second baseman Rodolfo Castro to first baseman Michael Chavis.

2022-09-15	SI	94.1	2313	Brubaker, JT(R)	Alonso, Pete(R)	86.8	12°	191	
3-1	Bot 3	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. Jeff McNeil to 3rd.

2022-09-15	SI	92.0	2257	Brubaker, JT(R)	Alonso, Pete(R)	--	°		
2-1	Bot 3	Ball	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. Jeff McNeil to 3rd.

2022-09-15	SI	92.0	2256	Brubaker, JT(R)	Alonso, Pete(R)	--	°		
2-0	Bot 3	Called Strike	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. Jeff McNeil to 3rd.

2022-09-15	SL	85.5	2652	Brubaker, JT(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Ball	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. Jeff McNeil to 3rd.

2022-09-15	SL	85.3	2548	Brubaker, JT(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Blocked Ball	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. Jeff McNeil to 3rd.

2022-09-15	ST	79.1	2274	Ramirez, Yohan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Hit By Pitch	
Pete Alonso hit by pitch. James McCann scores. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-09-15	SI	92.1	2147	Brubaker, JT(R)	Alonso, Pete(R)	73.3	52°	188	
0-0	Bot 1	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Cal Mitchell. Jeff McNeil to 3rd.

2022-09-15	ST	82.0	2348	Ramirez, Yohan(R)	Alonso, Pete(R)	--	°		
1-2	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-15	SI	95.1	2183	Ramirez, Yohan(R)	Alonso, Pete(R)	101.0	7°	136	
1-2	Bot 7	Foul	
Pete Alonso strikes out swinging.

2022-09-15	ST	82.6	2539	Ramirez, Yohan(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Ball	
Pete Alonso strikes out swinging.

2022-09-15	ST	81.6	2379	Ramirez, Yohan(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Called Strike	
Pete Alonso strikes out swinging.

2022-09-15	SI	95.6	2262	Ramirez, Yohan(R)	Alonso, Pete(R)	74.6	-50°	2	
0-0	Bot 7	Foul	
Pete Alonso strikes out swinging.

2022-09-14	KC	79.0	2205	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-09-14	SI	92.9	2022	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Ball	
Pete Alonso strikes out swinging.

2022-09-14	SI	92.6	2062	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Called Strike	
Pete Alonso strikes out swinging.

2022-09-14	SI	91.9	2061	Smyly, Drew(L)	Alonso, Pete(R)	70.8	42°	194	
0-0	Bot 4	Foul	
Pete Alonso strikes out swinging.

2022-09-14	SI	93.7	2184	Smyly, Drew(L)	Alonso, Pete(R)	92.0	-12°	12	
2-2	Bot 2	Hit Into Play	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SI	93.0	2069	Smyly, Drew(L)	Alonso, Pete(R)	75.7	17°	176	
2-2	Bot 2	Foul	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SI	92.8	1996	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
1-2	Bot 2	Ball	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	KC	79.3	2259	Smyly, Drew(L)	Alonso, Pete(R)	69.1	78°	99	
1-2	Bot 2	Foul	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SI	92.6	2176	Smyly, Drew(L)	Alonso, Pete(R)	73.5	23°	197	
1-1	Bot 2	Foul	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SI	92.1	2181	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
1-0	Bot 2	Called Strike	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SI	91.7	2177	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso grounds out, pitcher Drew Smyly to shortstop Christopher Morel to first baseman P. J. Higgins.

2022-09-14	SL	87.1	2334	Rucker, Michael(R)	Alonso, Pete(R)	109.7	20°	412	
1-2	Bot 8	Hit Into Play	
Pete Alonso homers (35) on a line drive to center field.

2022-09-14	CH	90.3	1746	Rucker, Michael(R)	Alonso, Pete(R)	65.1	-26°	2	
1-2	Bot 8	Foul	
Pete Alonso homers (35) on a line drive to center field.

2022-09-14	CH	90.3	1778	Rucker, Michael(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Swinging Strike	
Pete Alonso homers (35) on a line drive to center field.

2022-09-14	CH	89.1	1753	Rucker, Michael(R)	Alonso, Pete(R)	31.9	-23°	4	
1-0	Bot 8	Foul	
Pete Alonso homers (35) on a line drive to center field.

2022-09-14	SL	87.8	2309	Rucker, Michael(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso homers (35) on a line drive to center field.

2022-09-14	SI	93.9	2013	Uelmen, Erich(R)	Alonso, Pete(R)	99.3	18°	299	
1-1	Bot 6	Hit Into Play	
Pete Alonso lines out to right fielder Seiya Suzuki.

2022-09-14	SI	91.9	2077	Uelmen, Erich(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Foul	
Pete Alonso lines out to right fielder Seiya Suzuki.

2022-09-14	SI	93.1	2015	Uelmen, Erich(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso lines out to right fielder Seiya Suzuki.

2022-09-13	SI	92.4	1926	Sampson, Adrian(R)	Alonso, Pete(R)	100.0	50°	279	
3-2	Bot 6	Hit Into Play	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	FF	92.9	2002	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
3-2	Bot 6	Foul	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	CH	84.0	1779	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
2-2	Bot 6	Ball	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	SI	91.3	1984	Sampson, Adrian(R)	Alonso, Pete(R)	90.5	-11°	9	
2-2	Bot 6	Foul	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	SI	91.8	1970	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
2-1	Bot 6	Swinging Strike	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	FC	85.3	2464	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Ball	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	SI	91.7	1961	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Called Strike	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	SI	92.0	1912	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso flies out to center fielder Michael Hermosillo.

2022-09-13	FC	83.9	2509	Sampson, Adrian(R)	Alonso, Pete(R)	92.1	-3°	21	
0-0	Bot 3	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Zach McKinstry to second baseman David Bote. Jeff McNeil out at 2nd.

2022-09-13	SI	92.2	2111	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
3-1	Bot 1	Blocked Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-09-13	FF	93.1	2413	Hughes, Brandon(L)	Alonso, Pete(R)	112.4	28°	443	
0-1	Bot 9	Hit Into Play	
Pete Alonso homers (34) on a fly ball to center field.

2022-09-13	FF	92.3	2063	Sampson, Adrian(R)	Alonso, Pete(R)	109.2	41°	384	
3-0	Bot 1	Foul	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-09-13	SI	91.5	2008	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-09-13	FF	93.6	2316	Hughes, Brandon(L)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Called Strike	
Pete Alonso homers (34) on a fly ball to center field.

2022-09-13	SI	91.2	2085	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-09-13	FF	92.6	2045	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks. Jeff McNeil to 2nd.

2022-09-12	SL	80.4	2366	Assad, Javier(R)	Alonso, Pete(R)	88.7	-34°	3	
0-1	Bot 5	Hit Into Play	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-09-12	SI	91.7	1936	Assad, Javier(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-09-12	FC	88.1	2197	Assad, Javier(R)	Alonso, Pete(R)	88.0	42°	279	
0-0	Bot 3	Hit Into Play	
Pete Alonso flies out to right fielder Seiya Suzuki.

2022-09-12	SI	93.7	2139	Assad, Javier(R)	Alonso, Pete(R)	67.8	-30°	4	
1-0	Bot 1	Hit Into Play	
Pete Alonso grounds into a force out, third baseman Patrick Wisdom to second baseman Zach McKinstry. Francisco Lindor to 3rd. Jeff McNeil out at 2nd. Pete Alonso to 1st.

2022-09-12	SI	93.2	2064	Assad, Javier(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso grounds into a force out, third baseman Patrick Wisdom to second baseman Zach McKinstry. Francisco Lindor to 3rd. Jeff McNeil out at 2nd. Pete Alonso to 1st.

2022-09-12	SI	94.8	2038	Rodríguez, Manuel(R)	Alonso, Pete(R)	101.9	-3°	32	
0-0	Bot 8	Hit Into Play	
Pete Alonso singles on a sharp ground ball to left fielder Ian Happ. Jeff McNeil to 2nd.

2022-09-11	SI	95.0	2079	Luzardo, Jesús(L)	Alonso, Pete(R)	80.8	51°	227	
1-0	Top 3	Hit Into Play	
Pete Alonso flies out to center fielder JJ Bleday.

2022-09-11	CH	87.1	1888	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso flies out to center fielder JJ Bleday.

2022-09-11	SL	83.5	2311	Luzardo, Jesús(L)	Alonso, Pete(R)	94.3	53°	251	
2-2	Top 1	Hit Into Play	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	CH	87.8	1960	Luzardo, Jesús(L)	Alonso, Pete(R)	70.4	23°	187	
2-2	Top 1	Foul	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	FF	97.8	2297	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	SL	85.3	2311	Luzardo, Jesús(L)	Alonso, Pete(R)	91.3	-27°	3	
1-2	Top 1	Foul	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	SL	84.3	2361	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-2	Top 1	Blocked Ball	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	CH	87.6	1840	Luzardo, Jesús(L)	Alonso, Pete(R)	71.5	-50°	2	
0-2	Top 1	Foul	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	SI	97.7	2296	Luzardo, Jesús(L)	Alonso, Pete(R)	83.4	74°	140	
0-2	Top 1	Foul	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	SI	97.9	2414	Luzardo, Jesús(L)	Alonso, Pete(R)	--	°		
0-1	Top 1	Called Strike	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	FF	97.5	2305	Luzardo, Jesús(L)	Alonso, Pete(R)	87.0	55°	225	
0-0	Top 1	Foul	
Pete Alonso flies out to left fielder Jerar Encarnacion.

2022-09-11	FF	97.2	2611	Scott, Tanner(L)	Alonso, Pete(R)	66.6	14°	141	
0-2	Top 8	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Brian Anderson.

2022-09-11	FF	95.7	2580	Scott, Tanner(L)	Alonso, Pete(R)	79.5	61°	191	
0-1	Top 8	Foul	
Pete Alonso singles on a line drive to right fielder Brian Anderson.

2022-09-11	SL	89.2	2710	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Foul	
Pete Alonso singles on a line drive to right fielder Brian Anderson.

2022-09-11	CH	83.0	1507	Sulser, Cole(R)	Alonso, Pete(R)	93.5	4°	79	
2-2	Top 6	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Jerar Encarnacion.

2022-09-11	CH	82.2	1484	Sulser, Cole(R)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso singles on a ground ball to left fielder Jerar Encarnacion.

2022-09-11	FF	91.8	2055	Sulser, Cole(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Ball	
Pete Alonso singles on a ground ball to left fielder Jerar Encarnacion.

2022-09-11	SI	94.6	2228	Brazoban, Huascar(R)	Alonso, Pete(R)	90.9	-10°	14	
1-1	Top 4	Hit Into Play	
Pete Alonso grounds into a force out, fielded by second baseman Jon Berti. Tomas Nido scores. Brandon Nimmo to 3rd. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-09-11	SL	83.0	2215	Sulser, Cole(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Swinging Strike	
Pete Alonso singles on a ground ball to left fielder Jerar Encarnacion.

2022-09-11	SI	94.3	2174	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso grounds into a force out, fielded by second baseman Jon Berti. Tomas Nido scores. Brandon Nimmo to 3rd. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-09-11	FF	90.3	2159	Sulser, Cole(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso singles on a ground ball to left fielder Jerar Encarnacion.

2022-09-11	FC	86.9	2329	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso grounds into a force out, fielded by second baseman Jon Berti. Tomas Nido scores. Brandon Nimmo to 3rd. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-09-10	SI	94.8	2039	López, Pablo(R)	Alonso, Pete(R)	92.7	28°	353	
0-1	Top 4	Hit Into Play	
Pete Alonso flies out to left fielder Jon Berti.

2022-09-10	SI	94.7	2163	López, Pablo(R)	Alonso, Pete(R)	75.5	-35°	3	
0-0	Top 4	Foul	
Pete Alonso flies out to left fielder Jon Berti.

2022-09-10	FF	96.1	2226	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-2	Top 3	Called Strike	
Pete Alonso called out on strikes.

2022-09-10	CH	88.9	1920	López, Pablo(R)	Alonso, Pete(R)	85.1	-25°	3	
2-2	Top 3	Foul	
Pete Alonso called out on strikes.

2022-09-10	CH	88.5	2056	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-1	Top 3	Foul	
Pete Alonso called out on strikes.

2022-09-10	FF	95.2	2116	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-1	Top 3	Ball	
Pete Alonso called out on strikes.

2022-09-10	CH	90.1	1955	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-1	Top 3	Ball	
Pete Alonso called out on strikes.

2022-09-10	CH	89.2	2076	López, Pablo(R)	Alonso, Pete(R)	67.5	-32°	2	
0-0	Top 3	Foul	
Pete Alonso called out on strikes.

2022-09-10	FF	94.2	2351	Nardi, Andrew(L)	Alonso, Pete(R)	--	°		
1-2	Top 6	Called Strike	
Pete Alonso called out on strikes.

2022-09-10	SL	84.9	2139	Nardi, Andrew(L)	Alonso, Pete(R)	96.2	25°	311	
1-1	Top 6	Foul	
Pete Alonso called out on strikes.

2022-09-10	CH	89.3	1840	Nardi, Andrew(L)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso called out on strikes.

2022-09-10	SL	82.4	2265	Nardi, Andrew(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Swinging Strike	
Pete Alonso called out on strikes.

2022-09-10	SI	94.9	2109	López, Pablo(R)	Alonso, Pete(R)	95.6	1°	55	
1-0	Top 1	Hit Into Play	
Pete Alonso singles on a ground ball to center fielder JJ Bleday. Jeff McNeil to 2nd.

2022-09-10	CH	89.5	1983	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso singles on a ground ball to center fielder JJ Bleday. Jeff McNeil to 2nd.

2022-09-09	SL	87.8	2396	Cabrera, Edward(R)	Alonso, Pete(R)	115.6	21°	406	
2-2	Top 6	Hit Into Play	
Pete Alonso homers (33) on a line drive to left field. Brandon Nimmo scores.

2022-09-09	CU	87.0	2540	Cabrera, Edward(R)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso homers (33) on a line drive to left field. Brandon Nimmo scores.

2022-09-09	FF	96.1	2259	Cabrera, Edward(R)	Alonso, Pete(R)	74.1	46°	206	
1-1	Top 6	Foul	
Pete Alonso homers (33) on a line drive to left field. Brandon Nimmo scores.

2022-09-09	SL	87.5	2474	Cabrera, Edward(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Blocked Ball	
Pete Alonso homers (33) on a line drive to left field. Brandon Nimmo scores.

2022-09-09	SL	87.9	2538	Cabrera, Edward(R)	Alonso, Pete(R)	51.2	-55°	1	
0-0	Top 6	Foul	
Pete Alonso homers (33) on a line drive to left field. Brandon Nimmo scores.

2022-09-09	SI	95.9	2256	Cabrera, Edward(R)	Alonso, Pete(R)	71.8	41°	235	
1-1	Top 4	Hit Into Play	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-09	CH	90.7	1569	Cabrera, Edward(R)	Alonso, Pete(R)	104.9	-32°	4	
1-0	Top 4	Foul	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-09	CH	93.7	2216	Cabrera, Edward(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-09-09	SL	85.2	2234	Cabrera, Edward(R)	Alonso, Pete(R)	--	°		
0-2	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-09	SI	94.4	2173	Cabrera, Edward(R)	Alonso, Pete(R)	97.7	-10°	13	
0-1	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-09-09	SL	84.6	2250	Cabrera, Edward(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-09	SL	83.2	2485	Okert, Steven(L)	Alonso, Pete(R)	79.2	69°	134	
2-2	Top 8	Hit Into Play	
Pete Alonso pops out to first baseman Garrett Cooper in foul territory.

2022-09-09	SL	83.1	2504	Okert, Steven(L)	Alonso, Pete(R)	--	°		
1-2	Top 8	Ball	
Pete Alonso pops out to first baseman Garrett Cooper in foul territory.

2022-09-09	FF	94.9	2195	Okert, Steven(L)	Alonso, Pete(R)	--	°		
1-1	Top 8	Called Strike	
Pete Alonso pops out to first baseman Garrett Cooper in foul territory.

2022-09-09	SL	82.7	2353	Okert, Steven(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Swinging Strike	
Pete Alonso pops out to first baseman Garrett Cooper in foul territory.

2022-09-09	FF	95.0	2159	Okert, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso pops out to first baseman Garrett Cooper in foul territory.

2022-09-07	FF	91.7	2012	Wilson, Bryse(R)	Alonso, Pete(R)	79.0	42°	249	
0-2	Top 7	Hit Into Play	
Pete Alonso flies out to center fielder Jack Suwinski.

2022-09-07	SL	83.7	2205	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Called Strike	
Pete Alonso flies out to center fielder Jack Suwinski.

2022-09-07	SL	83.4	2145	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso flies out to center fielder Jack Suwinski.

2022-09-07	SL	86.0	2535	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
3-2	Top 2	Ball	
Pete Alonso walks.

2022-09-07	SL	88.1	2588	Oviedo, Johan(R)	Alonso, Pete(R)	70.0	15°	145	
3-2	Top 2	Foul	
Pete Alonso walks.

2022-09-07	SL	87.3	2572	Oviedo, Johan(R)	Alonso, Pete(R)	64.1	61°	151	
3-2	Top 2	Foul	
Pete Alonso walks.

2022-09-07	CH	89.9	1844	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Ball	
Pete Alonso walks.

2022-09-07	FF	97.1	2324	Oviedo, Johan(R)	Alonso, Pete(R)	73.3	36°	226	
2-1	Top 2	Foul	
Pete Alonso walks.

2022-09-07	SL	86.1	2579	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Ball	
Pete Alonso walks.

2022-09-07	FF	96.5	2369	Oviedo, Johan(R)	Alonso, Pete(R)	73.6	22°	196	
1-0	Top 2	Foul	
Pete Alonso walks.

2022-09-07	SL	89.6	2545	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso walks.

2022-09-07	FF	93.0	2138	Wilson, Bryse(R)	Alonso, Pete(R)	109.0	5°	152	
0-0	Top 4	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Cal Mitchell.

2022-09-07	SI	91.7	2225	Thompson, Zach(R)	Alonso, Pete(R)	101.8	2°	54	
0-1	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Ke'Bryan Hayes to first baseman Ben Gamel.

2022-09-07	FC	88.1	2557	Thompson, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Swinging Strike	
Pete Alonso grounds out, third baseman Ke'Bryan Hayes to first baseman Ben Gamel.

2022-09-07	FC	89.7	2301	Yajure, Miguel(R)	Alonso, Pete(R)	--	°		
3-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-07	FC	90.6	2348	Yajure, Miguel(R)	Alonso, Pete(R)	83.2	-22°	5	
3-1	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-09-07	SI	95.7	2195	Beede, Tyler(R)	Alonso, Pete(R)	112.5	-10°	11	
1-0	Top 7	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Cal Mitchell. Eduardo Escobar to 3rd. James McCann to 2nd.

2022-09-07	SL	82.8	2133	Wilson, Bryse(R)	Alonso, Pete(R)	84.6	59°	186	
0-2	Top 3	Hit Into Play	
Pete Alonso pops out to second baseman Tucupita Marcano.

2022-09-07	FC	90.7	2343	Yajure, Miguel(R)	Alonso, Pete(R)	--	°		
3-0	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-07	SL	83.3	2224	Wilson, Bryse(R)	Alonso, Pete(R)	67.8	11°	112	
0-1	Top 3	Foul	
Pete Alonso pops out to second baseman Tucupita Marcano.

2022-09-07	CU	78.3	2144	Beede, Tyler(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso singles on a ground ball to right fielder Cal Mitchell. Eduardo Escobar to 3rd. James McCann to 2nd.

2022-09-07	FF	92.8	2244	Yajure, Miguel(R)	Alonso, Pete(R)	--	°		
2-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-09-07	SL	83.5	2107	Wilson, Bryse(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso pops out to second baseman Tucupita Marcano.

2022-09-07	FC	90.3	2326	Yajure, Miguel(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-09-07	FC	89.6	2328	Yajure, Miguel(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-09-07	FF	97.5	2474	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Called Strike	
Pete Alonso called out on strikes.

2022-09-07	SL	86.1	2688	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso called out on strikes.

2022-09-07	FF	96.7	2432	Oviedo, Johan(R)	Alonso, Pete(R)	74.3	16°	164	
1-2	Top 1	Foul	
Pete Alonso called out on strikes.

2022-09-07	CU	75.6	2051	Thompson, Zach(R)	Alonso, Pete(R)	87.0	7°	129	
1-1	Top 4	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. James McCann to 2nd.

2022-09-07	FC	88.8	2462	Thompson, Zach(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. James McCann to 2nd.

2022-09-07	SL	86.2	2716	Oviedo, Johan(R)	Alonso, Pete(R)	35.5	-17°	8	
1-2	Top 1	Foul	
Pete Alonso called out on strikes.

2022-09-07	CU	75.3	1972	Thompson, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso singles on a line drive to left fielder Jack Suwinski. James McCann to 2nd.

2022-09-07	CH	88.6	1739	Oviedo, Johan(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso called out on strikes.

2022-09-07	SI	94.6	2121	Underwood Jr., Duane(R)	Alonso, Pete(R)	113.3	3°	99	
2-0	Top 1	Hit Into Play	
Pete Alonso doubles (24) on a ground ball to left fielder Greg Allen. Brandon Nimmo to 3rd.

2022-09-07	SL	85.9	2582	Oviedo, Johan(R)	Alonso, Pete(R)	73.1	71°	134	
0-1	Top 1	Foul	
Pete Alonso called out on strikes.

2022-09-07	FC	92.5	2217	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso doubles (24) on a ground ball to left fielder Greg Allen. Brandon Nimmo to 3rd.

2022-09-07	FF	95.7	2185	Oviedo, Johan(R)	Alonso, Pete(R)	112.7	22°	379	
0-0	Top 1	Foul	
Pete Alonso called out on strikes.

2022-09-07	SI	95.2	2107	Underwood Jr., Duane(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso doubles (24) on a ground ball to left fielder Greg Allen. Brandon Nimmo to 3rd.

2022-09-06	ST	84.5	2811	Keller, Mitch(R)	Alonso, Pete(R)	76.8	13°	175	
2-2	Top 6	Hit Into Play	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	SI	95.1	2333	Keller, Mitch(R)	Alonso, Pete(R)	70.4	-40°	2	
2-2	Top 6	Foul	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	ST	83.7	2772	Keller, Mitch(R)	Alonso, Pete(R)	99.6	39°	348	
2-2	Top 6	Foul	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	FF	95.1	2405	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	ST	84.4	2863	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Swinging Strike	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	SI	94.3	2496	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	SI	93.4	2530	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso lines out to second baseman Kevin Newman.

2022-09-06	ST	83.6	2868	Keller, Mitch(R)	Alonso, Pete(R)	78.8	2°	55	
0-1	Top 3	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Oneil Cruz to second baseman Kevin Newman to first baseman Michael Chavis. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-09-06	ST	83.8	2812	Keller, Mitch(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso grounds into a double play, shortstop Oneil Cruz to second baseman Kevin Newman to first baseman Michael Chavis. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-09-06	SI	94.4	2397	Keller, Mitch(R)	Alonso, Pete(R)	75.4	-40°	2	
0-1	Top 1	Hit Into Play	
Pete Alonso grounds into a double play, third baseman Ke'Bryan Hayes to second baseman Kevin Newman to first baseman Michael Chavis. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-09-06	ST	82.8	2785	Keller, Mitch(R)	Alonso, Pete(R)	64.1	68°	112	
0-0	Top 1	Foul	
Pete Alonso grounds into a double play, third baseman Ke'Bryan Hayes to second baseman Kevin Newman to first baseman Michael Chavis. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-09-06	CU	80.8	2517	Bañuelos, Manny(L)	Alonso, Pete(R)	74.1	4°	62	
2-0	Top 8	Hit Into Play	
Pete Alonso grounds out, second baseman Kevin Newman to first baseman Michael Chavis.

2022-09-06	FF	94.8	2113	Bañuelos, Manny(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso grounds out, second baseman Kevin Newman to first baseman Michael Chavis.

2022-09-06	CU	80.1	2522	Bañuelos, Manny(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso grounds out, second baseman Kevin Newman to first baseman Michael Chavis.

2022-09-04	SI	93.9	1977	Fedde, Erick(R)	Alonso, Pete(R)	81.2	-1°	40	
2-1	Bot 6	Hit Into Play	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-04	CH	87.8	1564	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Ball	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-04	SI	93.3	1934	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Foul Tip	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-04	FC	89.4	2152	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-04	FC	89.6	2150	Fedde, Erick(R)	Alonso, Pete(R)	95.8	52°	257	
1-1	Bot 4	Hit Into Play	
Pete Alonso flies out to center fielder Victor Robles.

2022-09-04	SI	92.4	1860	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-09-04	SI	92.1	1811	Fedde, Erick(R)	Alonso, Pete(R)	92.0	33°	297	
0-0	Bot 4	Foul	
Pete Alonso flies out to center fielder Victor Robles.

2022-09-04	SI	93.6	1800	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
3-2	Bot 2	Ball	
Pete Alonso walks.

2022-09-04	SI	93.6	1869	Fedde, Erick(R)	Alonso, Pete(R)	71.0	60°	146	
3-1	Bot 2	Foul	
Pete Alonso walks.

2022-09-04	SI	93.7	1943	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
2-1	Bot 2	Ball	
Pete Alonso walks.

2022-09-04	CU	79.6	2313	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
2-0	Bot 2	Called Strike	
Pete Alonso walks.

2022-09-04	SI	90.2	1833	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-0	Bot 2	Ball	
Pete Alonso walks.

2022-09-04	SI	91.0	1837	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso walks.

2022-09-04	FF	92.6	2280	Abbott, Cory(R)	Alonso, Pete(R)	86.7	51°	230	
0-0	Bot 9	Hit Into Play	
Pete Alonso flies out to left fielder Josh Palacios.

2022-09-03	SI	94.0	2085	Corbin, Patrick(L)	Alonso, Pete(R)	86.6	6°	97	
1-0	Bot 6	Hit Into Play	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-03	SI	92.9	2124	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso grounds out, shortstop CJ Abrams to first baseman Joey Meneses.

2022-09-03	SI	95.5	2052	Corbin, Patrick(L)	Alonso, Pete(R)	55.0	1°	35	
3-2	Bot 4	Hit Into Play	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	95.4	2089	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-2	Bot 4	Ball	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	95.2	2157	Corbin, Patrick(L)	Alonso, Pete(R)	59.1	67°	112	
2-2	Bot 4	Foul	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	94.7	2148	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Ball	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	FF	92.4	2082	Corbin, Patrick(L)	Alonso, Pete(R)	70.1	73°	119	
1-1	Bot 4	Foul	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	92.8	1971	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Called Strike	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	93.5	1999	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso grounds out softly, third baseman Ildemaro Vargas to first baseman Joey Meneses.

2022-09-03	SI	95.0	2160	Corbin, Patrick(L)	Alonso, Pete(R)	104.1	34°	391	
2-2	Bot 1	Hit Into Play	
Pete Alonso flies out sharply to center fielder Lane Thomas.

2022-09-03	SL	83.7	2049	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Blocked Ball	
Pete Alonso flies out sharply to center fielder Lane Thomas.

2022-09-03	SI	94.6	2169	Corbin, Patrick(L)	Alonso, Pete(R)	61.7	34°	145	
1-1	Bot 1	Foul	
Pete Alonso flies out sharply to center fielder Lane Thomas.

2022-09-03	SI	94.3	2069	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Foul	
Pete Alonso flies out sharply to center fielder Lane Thomas.

2022-09-03	FF	93.5	2060	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out sharply to center fielder Lane Thomas.

2022-09-03	FC	89.4	2344	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-2	Bot 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-03	SI	94.2	2291	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 9	Called Strike	
Pete Alonso strikes out swinging.

2022-09-03	SI	93.8	2280	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Called Strike	
Pete Alonso strikes out swinging.

2022-09-02	SI	93.4	2421	Gray, Josiah(R)	Alonso, Pete(R)	105.8	36°	375	
1-0	Bot 6	Hit Into Play	
Pete Alonso homers (32) on a fly ball to left center field.

2022-09-02	SL	84.2	2038	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso homers (32) on a fly ball to left center field.

2022-09-02	SI	94.7	2317	Gray, Josiah(R)	Alonso, Pete(R)	103.3	-16°	9	
0-0	Bot 3	Hit Into Play	
Pete Alonso grounds out sharply, third baseman Ildemaro Vargas to first baseman Luke Voit.

2022-09-02	FF	97.0	2456	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks.

2022-09-02	SL	87.1	2034	Gray, Josiah(R)	Alonso, Pete(R)	99.8	7°	136	
3-2	Bot 1	Foul	
Pete Alonso walks.

2022-09-02	CU	84.3	2602	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Blocked Ball	
Pete Alonso walks.

2022-09-02	SL	87.1	2113	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Foul	
Pete Alonso walks.

2022-09-02	SL	86.3	2085	Gray, Josiah(R)	Alonso, Pete(R)	96.9	31°	333	
2-2	Bot 1	Foul	
Pete Alonso walks.

2022-09-02	SL	87.3	2087	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso walks.

2022-09-02	SL	86.0	2022	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Swinging Strike	
Pete Alonso walks.

2022-09-02	SL	87.1	2034	Gray, Josiah(R)	Alonso, Pete(R)	--	°	9	
1-0	Bot 1	Swinging Strike	
Pete Alonso walks.

2022-09-02	FF	96.3	2325	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks.

2022-09-02	SI	97.3	2339	Thompson, Mason(R)	Alonso, Pete(R)	51.1	7°	59	
0-1	Bot 7	Hit Into Play	
Pete Alonso grounds out softly, second baseman Luis Garcia to first baseman Luke Voit.

2022-09-02	SL	85.6	2212	Thompson, Mason(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso grounds out softly, second baseman Luis Garcia to first baseman Luke Voit.

2022-09-01	SL	87.1	2691	Kershaw, Clayton(L)	Alonso, Pete(R)	107.0	4°	96	
0-2	Bot 3	Hit Into Play	
Pete Alonso grounds out, shortstop Trea Turner to first baseman Freddie Freeman.

2022-09-01	FF	91.4	2432	Kershaw, Clayton(L)	Alonso, Pete(R)	65.7	48°	165	
0-2	Bot 3	Foul	
Pete Alonso grounds out, shortstop Trea Turner to first baseman Freddie Freeman.

2022-09-01	CU	74.3	2433	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Called Strike	
Pete Alonso grounds out, shortstop Trea Turner to first baseman Freddie Freeman.

2022-09-01	FF	91.3	2389	Kershaw, Clayton(L)	Alonso, Pete(R)	104.3	32°	354	
0-0	Bot 3	Foul	
Pete Alonso grounds out, shortstop Trea Turner to first baseman Freddie Freeman.

2022-09-01	FF	93.0	2343	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Blocked Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	91.3	2336	Kershaw, Clayton(L)	Alonso, Pete(R)	71.0	18°	164	
3-1	Bot 1	Foul	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	95.3	2267	Martin, Chris(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-01	FF	90.4	2220	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	94.7	2254	Martin, Chris(R)	Alonso, Pete(R)	--	°		
0-2	Bot 6	Ball	
Pete Alonso strikes out swinging.

2022-09-01	FF	91.6	2364	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Swinging Strike	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	94.9	2260	Martin, Chris(R)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-01	SI	95.5	2295	Martin, Chris(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-09-01	FF	90.8	2278	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	90.9	2300	Kershaw, Clayton(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-09-01	FF	95.3	2293	Hembree, Heath(R)	Alonso, Pete(R)	87.1	60°	173	
2-2	Bot 8	Hit Into Play	
Pete Alonso pops out to second baseman Gavin Lux.

2022-09-01	FF	92.3	2218	Hembree, Heath(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Called Strike	
Pete Alonso pops out to second baseman Gavin Lux.

2022-09-01	SL	84.7	2729	Hembree, Heath(R)	Alonso, Pete(R)	87.0	51°	251	
2-0	Bot 8	Foul	
Pete Alonso pops out to second baseman Gavin Lux.

2022-09-01	FF	93.5	2383	Hembree, Heath(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso pops out to second baseman Gavin Lux.

2022-09-01	SL	84.5	2706	Hembree, Heath(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso pops out to second baseman Gavin Lux.

2022-08-31	FC	87.7	2462	Anderson, Tyler(L)	Alonso, Pete(R)	102.3	-6°	23	
2-2	Bot 6	Hit Into Play	
Pete Alonso grounds out sharply, third baseman Justin Turner to first baseman Freddie Freeman.

2022-08-31	CH	79.3	1862	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso grounds out sharply, third baseman Justin Turner to first baseman Freddie Freeman.

2022-08-31	FF	91.9	2270	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
0-2	Bot 6	Ball	
Pete Alonso grounds out sharply, third baseman Justin Turner to first baseman Freddie Freeman.

2022-08-31	FC	87.1	2396	Anderson, Tyler(L)	Alonso, Pete(R)	--	°	15	
0-1	Bot 6	Swinging Strike	
Pete Alonso grounds out sharply, third baseman Justin Turner to first baseman Freddie Freeman.

2022-08-31	FF	90.0	2290	Anderson, Tyler(L)	Alonso, Pete(R)	38.7	-30°	6	
0-0	Bot 6	Foul	
Pete Alonso grounds out sharply, third baseman Justin Turner to first baseman Freddie Freeman.

2022-08-31	FF	89.9	2403	Anderson, Tyler(L)	Alonso, Pete(R)	84.6	13°	188	
0-0	Bot 3	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Mookie Betts. Francisco Lindor to 2nd.

2022-08-31	CH	79.4	1959	Anderson, Tyler(L)	Alonso, Pete(R)	78.9	39°	257	
3-2	Bot 1	Hit Into Play	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	FF	91.4	2369	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	FF	90.4	2255	Anderson, Tyler(L)	Alonso, Pete(R)	71.6	51°	208	
2-1	Bot 1	Foul	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	CH	76.7	1779	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Called Strike	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	FF	90.3	2210	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	CH	76.7	1814	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out to left fielder Joey Gallo.

2022-08-31	SI	92.2	2120	Reed, Jake(R)	Alonso, Pete(R)	100.3	42°	313	
0-0	Bot 8	Hit Into Play	
Pete Alonso flies out sharply to right fielder Mookie Betts.

2022-08-30	FF	93.8	2515	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.5	2481	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
2-1	Bot 5	Foul Tip	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.6	2435	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.1	2423	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.5	2479	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.9	2461	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.2	2464	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.2	2451	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.3	2393	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso strikes out swinging.

2022-08-30	FF	94.8	2368	Vesia, Alex(L)	Alonso, Pete(R)	95.7	41°	304	
0-0	Bot 7	Hit Into Play	
Pete Alonso flies out to right fielder Mookie Betts.

2022-08-30	FF	94.7	2524	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.8	2489	Heaney, Andrew(L)	Alonso, Pete(R)	69.2	28°	164	
2-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.4	2449	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.3	2471	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-30	FF	93.7	2470	Heaney, Andrew(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-08-28	KC	86.7	2555	Márquez, Germán(R)	Alonso, Pete(R)	97.0	47°	278	
0-1	Bot 7	Hit Into Play	
Pete Alonso flies out to center fielder Garrett Hampson.

2022-08-28	SI	95.1	2158	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso flies out to center fielder Garrett Hampson.

2022-08-28	SL	88.7	2441	Márquez, Germán(R)	Alonso, Pete(R)	107.4	2°	85	
0-2	Bot 4	Hit Into Play	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-08-28	FF	95.9	2053	Márquez, Germán(R)	Alonso, Pete(R)	71.1	65°	149	
0-2	Bot 4	Foul	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-08-28	KC	87.1	2676	Márquez, Germán(R)	Alonso, Pete(R)	57.9	41°	141	
0-2	Bot 4	Foul	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-08-28	SI	95.9	2032	Márquez, Germán(R)	Alonso, Pete(R)	68.8	32°	162	
0-1	Bot 4	Foul	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-08-28	SL	88.9	2395	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Swinging Strike	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-08-28	SI	94.6	2106	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
3-1	Bot 1	Blocked Ball	
Pete Alonso walks.

2022-08-28	FF	96.2	2176	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
3-0	Bot 1	Called Strike	
Pete Alonso walks.

2022-08-28	SI	95.6	1971	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso walks.

2022-08-28	SL	89.2	2320	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso walks.

2022-08-28	FF	95.6	1998	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks.

2022-08-28	SI	99.6	2603	Bard, Daniel(R)	Alonso, Pete(R)	74.8	27°	224	
0-0	Bot 9	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Randal Grichuk.

2022-08-27	SL	85.2	2252	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-27	SI	90.7	2433	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-27	SL	86.4	2428	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-08-27	SI	91.2	2443	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-27	SI	90.5	2528	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-27	SI	89.6	2376	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-08-27	SI	89.7	2489	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-27	ST	83.9	3018	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-27	ST	83.5	2845	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-27	ST	81.4	2851	Lawrence, Justin(R)	Alonso, Pete(R)	64.1	17°	149	
0-0	Bot 7	Foul	
Pete Alonso strikes out swinging.

2022-08-27	SL	85.9	2385	Freeland, Kyle(L)	Alonso, Pete(R)	100.1	14°	219	
3-2	Bot 1	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	CH	87.6	1543	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	KC	81.1	2456	Freeland, Kyle(L)	Alonso, Pete(R)	52.1	-21°	6	
2-2	Bot 1	Foul	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	SL	85.8	2281	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	KC	81.4	2467	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Foul	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	SI	89.7	2357	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	SL	85.8	2475	Freeland, Kyle(L)	Alonso, Pete(R)	100.3	-4°	22	
0-1	Bot 1	Foul	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	SI	89.6	2440	Freeland, Kyle(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Swinging Strike	
Pete Alonso singles on a sharp line drive to left fielder Wynton Bernard.

2022-08-27	SI	93.3	2231	Lawrence, Justin(R)	Alonso, Pete(R)	93.2	28°	347	
1-1	Bot 6	Hit Into Play	
Pete Alonso flies out to left fielder Wynton Bernard.

2022-08-27	SI	95.3	2128	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso flies out to left fielder Wynton Bernard.

2022-08-27	SI	94.8	2126	Lawrence, Justin(R)	Alonso, Pete(R)	75.4	-36°	4	
0-0	Bot 6	Foul	
Pete Alonso flies out to left fielder Wynton Bernard.

2022-08-26	SL	87.6	2363	Kuhl, Chad(R)	Alonso, Pete(R)	101.7	12°	238	
1-0	Bot 4	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Connor Joe.

2022-08-26	KC	78.4	2832	Kuhl, Chad(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso singles on a sharp line drive to left fielder Connor Joe.

2022-08-26	SL	88.3	2756	Bard, Daniel(R)	Alonso, Pete(R)	100.9	-6°	19	
0-2	Bot 9	Hit Into Play	
Pete Alonso singles on a sharp ground ball to left fielder Sam Hilliard. Brandon Nimmo scores. Starling Marte to 2nd.

2022-08-26	SI	98.5	2479	Bard, Daniel(R)	Alonso, Pete(R)	--	°		
0-1	Bot 9	Called Strike	
Pete Alonso singles on a sharp ground ball to left fielder Sam Hilliard. Brandon Nimmo scores. Starling Marte to 2nd.

2022-08-26	SL	88.8	2666	Bard, Daniel(R)	Alonso, Pete(R)	65.5	44°	175	
0-0	Bot 9	Foul	
Pete Alonso singles on a sharp ground ball to left fielder Sam Hilliard. Brandon Nimmo scores. Starling Marte to 2nd.

2022-08-26	SL	87.0	2709	Kuhl, Chad(R)	Alonso, Pete(R)	82.2	33°	298	
0-1	Bot 1	Hit Into Play	
Pete Alonso flies out to left fielder Connor Joe.

2022-08-26	SI	94.1	1941	Kuhl, Chad(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso flies out to left fielder Connor Joe.

2022-08-26	FF	98.6	2346	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-08-26	FF	98.1	2349	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Swinging Strike	
Pete Alonso strikes out on a foul tip.

2022-08-26	FF	94.6	2332	Gilbreath, Lucas(L)	Alonso, Pete(R)	87.8	18°	268	
2-2	Bot 6	Hit Into Play	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	SL	89.4	2206	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso strikes out on a foul tip.

2022-08-26	FF	98.7	2283	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-08-26	FF	95.9	2423	Gilbreath, Lucas(L)	Alonso, Pete(R)	--	°		
2-2	Bot 6	Foul	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	SL	83.5	2442	Gilbreath, Lucas(L)	Alonso, Pete(R)	71.2	8°	91	
2-2	Bot 6	Foul	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	FF	98.9	2184	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso strikes out on a foul tip.

2022-08-26	FF	94.6	2440	Gilbreath, Lucas(L)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	FF	94.7	2381	Gilbreath, Lucas(L)	Alonso, Pete(R)	--	°		
0-2	Bot 6	Ball	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	SL	84.4	2503	Gilbreath, Lucas(L)	Alonso, Pete(R)	111.6	12°	245	
0-1	Bot 6	Foul	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-26	FF	94.9	2453	Gilbreath, Lucas(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso lines out to right fielder Randal Grichuk.

2022-08-25	FF	94.2	2372	Feltner, Ryan(R)	Alonso, Pete(R)	106.7	32°	409	
3-0	Bot 3	Hit Into Play	
Pete Alonso homers (31) on a fly ball to left center field. Starling Marte scores.

2022-08-25	FF	95.5	2293	Feltner, Ryan(R)	Alonso, Pete(R)	--	°		
2-0	Bot 3	Ball	
Pete Alonso homers (31) on a fly ball to left center field. Starling Marte scores.

2022-08-25	SL	84.7	2459	Feltner, Ryan(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Ball	
Pete Alonso homers (31) on a fly ball to left center field. Starling Marte scores.

2022-08-25	SL	85.7	2394	Feltner, Ryan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso homers (31) on a fly ball to left center field. Starling Marte scores.

2022-08-25	SI	94.4	2320	Feltner, Ryan(R)	Alonso, Pete(R)	113.0	5°	129	
1-0	Bot 2	Hit Into Play	
Pete Alonso singles on a sharp ground ball to left fielder Sam Hilliard.

2022-08-25	SI	93.6	2367	Feltner, Ryan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso singles on a sharp ground ball to left fielder Sam Hilliard.

2022-08-25	ST	82.0	2692	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
2-2	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging. Francisco Lindor to 2nd. Starling Marte steals (18) 3rd base. Francisco Lindor steals (14) 2nd base.

2022-08-25	SI	93.2	2135	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
2-1	Bot 7	Called Strike	
Pete Alonso strikes out swinging. Francisco Lindor to 2nd. Starling Marte steals (18) 3rd base. Francisco Lindor steals (14) 2nd base.

2022-08-25	SI	94.7	2286	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
1-1	Bot 7	Ball	
Pete Alonso strikes out swinging. Francisco Lindor to 2nd. Starling Marte steals (18) 3rd base. Francisco Lindor steals (14) 2nd base.

2022-08-25	SI	93.2	2272	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Called Strike	
Pete Alonso strikes out swinging. Francisco Lindor to 2nd. Starling Marte steals (18) 3rd base. Francisco Lindor steals (14) 2nd base.

2022-08-25	FC	90.0	2374	Bird, Jake(R)	Alonso, Pete(R)	87.7	38°	289	
1-0	Bot 5	Hit Into Play	
Pete Alonso flies out to right fielder Randal Grichuk.

2022-08-25	ST	79.0	2619	Lawrence, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso strikes out swinging. Francisco Lindor to 2nd. Starling Marte steals (18) 3rd base. Francisco Lindor steals (14) 2nd base.

2022-08-25	SI	94.9	1917	Bird, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso flies out to right fielder Randal Grichuk.

2022-08-23	SI	96.5	2380	Montas, Frankie(R)	Alonso, Pete(R)	115.8	-2°	30	
2-0	Top 6	Hit Into Play	
Pete Alonso singles on a sharp ground ball to center fielder Aaron Judge.

2022-08-23	SI	95.7	2309	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso singles on a sharp ground ball to center fielder Aaron Judge.

2022-08-23	SL	88.4	2460	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso singles on a sharp ground ball to center fielder Aaron Judge.

2022-08-23	FF	98.2	2423	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
2-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-23	FC	89.0	2446	Montas, Frankie(R)	Alonso, Pete(R)	100.9	-16°	6	
2-1	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-08-23	FF	96.7	2393	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-08-23	SI	96.1	2232	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-08-23	SI	95.1	2268	Montas, Frankie(R)	Alonso, Pete(R)	80.4	84°	86	
0-0	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-08-23	ST	86.6	2840	Schmidt, Clarke(R)	Alonso, Pete(R)	107.1	7°	164	
0-2	Top 8	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Andrew Benintendi. Francisco Lindor to 2nd.

2022-08-23	ST	87.9	2912	Schmidt, Clarke(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Foul Tip	
Pete Alonso singles on a sharp line drive to left fielder Andrew Benintendi. Francisco Lindor to 2nd.

2022-08-23	ST	87.2	2876	Schmidt, Clarke(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso singles on a sharp line drive to left fielder Andrew Benintendi. Francisco Lindor to 2nd.

2022-08-23	SL	88.5	2420	Montas, Frankie(R)	Alonso, Pete(R)	83.6	78°	73	
3-1	Top 1	Hit Into Play	
Pete Alonso pops out to first baseman Anthony Rizzo in foul territory.

2022-08-23	SI	95.9	2241	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Ball	
Pete Alonso pops out to first baseman Anthony Rizzo in foul territory.

2022-08-23	SI	94.9	2239	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso pops out to first baseman Anthony Rizzo in foul territory.

2022-08-23	SI	96.7	2276	Montas, Frankie(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Ball	
Pete Alonso pops out to first baseman Anthony Rizzo in foul territory.

2022-08-23	SL	88.1	2385	Montas, Frankie(R)	Alonso, Pete(R)	--	°	4	
0-0	Top 1	Swinging Strike	
Pete Alonso pops out to first baseman Anthony Rizzo in foul territory.

2022-08-22	FF	93.5	2453	Germán, Domingo(R)	Alonso, Pete(R)	96.8	56°	219	
1-0	Top 7	Hit Into Play	
Pete Alonso reaches on a fielding error by second baseman Oswaldo Cabrera.

2022-08-22	CU	81.7	2528	Germán, Domingo(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso reaches on a fielding error by second baseman Oswaldo Cabrera.

2022-08-22	SI	93.2	2415	Germán, Domingo(R)	Alonso, Pete(R)	105.9	-16°	9	
1-1	Top 4	Hit Into Play	
Pete Alonso grounds into a double play, second baseman Oswaldo Cabrera to first baseman Anthony Rizzo. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-22	CU	79.9	2403	Germán, Domingo(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Called Strike	
Pete Alonso grounds into a double play, second baseman Oswaldo Cabrera to first baseman Anthony Rizzo. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-22	CU	80.7	2482	Germán, Domingo(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Blocked Ball	
Pete Alonso grounds into a double play, second baseman Oswaldo Cabrera to first baseman Anthony Rizzo. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-22	SI	92.2	2589	Germán, Domingo(R)	Alonso, Pete(R)	32.0	32°	60	
0-0	Top 2	Hit Into Play	
Pete Alonso grounds out, third baseman Josh Donaldson to first baseman Anthony Rizzo.

2022-08-22	CU	88.4	2550	Loáisiga, Jonathan(R)	Alonso, Pete(R)	80.9	41°	254	
1-1	Top 9	Hit Into Play	
Pete Alonso flies out to center fielder Aaron Judge.

2022-08-22	SI	99.1	2313	Loáisiga, Jonathan(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Swinging Strike	
Pete Alonso flies out to center fielder Aaron Judge.

2022-08-22	SI	98.9	2178	Loáisiga, Jonathan(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso flies out to center fielder Aaron Judge.

2022-08-21	SI	94.4	2126	Gibson, Kyle(R)	Alonso, Pete(R)	100.4	-16°	6	
2-1	Top 4	Hit Into Play	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-21	SL	84.2	2509	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
2-0	Top 4	Swinging Strike	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-21	SI	93.1	2051	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-21	FC	91.3	2303	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-21	SL	84.2	2593	Gibson, Kyle(R)	Alonso, Pete(R)	104.2	-4°	24	
2-2	Top 3	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	FF	92.5	2018	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Ball	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	SI	92.8	2140	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Foul	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	FC	91.4	2230	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Top 3	Swinging Strike	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	SL	84.0	2488	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Top 3	Blocked Ball	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	SI	92.9	2194	Gibson, Kyle(R)	Alonso, Pete(R)	66.6	-27°	5	
0-0	Top 3	Foul	
Pete Alonso grounds into a double play, shortstop Bryson Stott to second baseman Nick Maton to first baseman Rhys Hoskins. Starling Marte to 3rd. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-21	SI	93.2	2182	Gibson, Kyle(R)	Alonso, Pete(R)	109.0	11°	275	
2-1	Top 1	Hit Into Play	
Pete Alonso lines out sharply to right fielder Nick Castellanos.

2022-08-21	FC	90.6	2382	Gibson, Kyle(R)	Alonso, Pete(R)	66.8	55°	169	
2-0	Top 1	Foul	
Pete Alonso lines out sharply to right fielder Nick Castellanos.

2022-08-21	SL	83.5	2527	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso lines out sharply to right fielder Nick Castellanos.

2022-08-21	FC	90.6	2305	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso lines out sharply to right fielder Nick Castellanos.

2022-08-21	FC	89.0	2434	Brogdon, Connor(R)	Alonso, Pete(R)	77.7	10°	161	
1-0	Top 7	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Bradley Zimmer.

2022-08-21	FF	94.6	2290	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso singles on a line drive to center fielder Bradley Zimmer.

2022-08-20	SL	88.8	2454	Wheeler, Zack(R)	Alonso, Pete(R)	83.6	58°	198	
1-0	Top 6	Hit Into Play	
Pete Alonso pops out to second baseman Jean Segura.

2022-08-20	SI	95.9	2224	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso pops out to second baseman Jean Segura.

2022-08-20	FF	92.3	2091	Falter, Bailey(L)	Alonso, Pete(R)	76.1	37°	261	
0-2	Top 6	Hit Into Play	
Pete Alonso flies out to center fielder Matt Vierling.

2022-08-20	FF	91.8	2062	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-1	Top 6	Foul	
Pete Alonso flies out to center fielder Matt Vierling.

2022-08-20	CU	76.6	2076	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso flies out to center fielder Matt Vierling.

2022-08-20	SI	96.2	2308	Wheeler, Zack(R)	Alonso, Pete(R)	97.6	-25°	5	
1-0	Top 4	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Bryson Stott to second baseman Jean Segura. Starling Marte out at 2nd. Pete Alonso to 1st.

2022-08-20	FF	96.0	2522	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso grounds into a force out, shortstop Bryson Stott to second baseman Jean Segura. Starling Marte out at 2nd. Pete Alonso to 1st.

2022-08-20	CU	77.7	2166	Falter, Bailey(L)	Alonso, Pete(R)	100.0	35°	382	
0-2	Top 4	Hit Into Play	
Pete Alonso flies out sharply to center fielder Matt Vierling.

2022-08-20	FF	92.0	2045	Falter, Bailey(L)	Alonso, Pete(R)	82.6	51°	234	
0-1	Top 4	Foul	
Pete Alonso flies out sharply to center fielder Matt Vierling.

2022-08-20	SI	90.4	1586	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Foul	
Pete Alonso flies out sharply to center fielder Matt Vierling.

2022-08-20	SL	92.3	2395	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
3-1	Top 9	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SL	92.2	2239	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SL	91.5	2296	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	FF	97.2	2285	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SL	91.6	2383	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	FC	85.8	2423	Brogdon, Connor(R)	Alonso, Pete(R)	95.3	36°	339	
1-0	Top 7	Hit Into Play	
Pete Alonso flies out to center fielder Bradley Zimmer.

2022-08-20	FF	94.1	2410	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso flies out to center fielder Bradley Zimmer.

2022-08-20	FC	93.4	2553	Robertson, David(R)	Alonso, Pete(R)	97.9	63°	179	
3-1	Top 9	Hit Into Play	
Pete Alonso pops out to shortstop Edmundo Sosa.

2022-08-20	FC	92.4	2541	Robertson, David(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Ball	
Pete Alonso pops out to shortstop Edmundo Sosa.

2022-08-20	FC	92.3	2535	Robertson, David(R)	Alonso, Pete(R)	67.1	50°	177	
2-0	Top 9	Foul	
Pete Alonso pops out to shortstop Edmundo Sosa.

2022-08-20	FF	91.6	2242	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
3-2	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	FF	91.9	2209	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
3-1	Top 1	Foul Tip	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SL	85.0	2549	Robertson, David(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso pops out to shortstop Edmundo Sosa.

2022-08-20	SL	89.1	2648	Wheeler, Zack(R)	Alonso, Pete(R)	73.9	-20°	6	
1-1	Top 1	Hit Into Play	
Pete Alonso grounds out to pitcher Zack Wheeler.

2022-08-20	FC	91.6	2425	Robertson, David(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso pops out to shortstop Edmundo Sosa.

2022-08-20	SI	91.0	1964	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
3-0	Top 1	Called Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SI	94.8	2226	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Ball	
Pete Alonso grounds out to pitcher Zack Wheeler.

2022-08-20	FF	91.4	2209	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
2-0	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	SL	89.2	2560	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso grounds out to pitcher Zack Wheeler.

2022-08-20	FF	91.4	2124	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-20	FF	90.8	2255	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-19	KC	78.8	2596	Nola, Aaron(R)	Alonso, Pete(R)	82.8	59°	175	
0-2	Top 5	Hit Into Play	
Pete Alonso pops out to shortstop Bryson Stott.

2022-08-19	FC	85.9	2175	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Swinging Strike	
Pete Alonso pops out to shortstop Bryson Stott.

2022-08-19	FF	92.0	2211	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso pops out to shortstop Bryson Stott.

2022-08-19	FF	92.1	2392	Nola, Aaron(R)	Alonso, Pete(R)	100.6	39°	353	
2-2	Top 3	Hit Into Play	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	KC	78.2	2647	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Ball	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	FF	94.8	2409	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Foul	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	KC	79.5	2696	Nola, Aaron(R)	Alonso, Pete(R)	39.8	-28°	4	
1-1	Top 3	Foul	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	FF	94.2	2447	Nola, Aaron(R)	Alonso, Pete(R)	70.7	16°	155	
1-0	Top 3	Foul	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	FF	93.9	2460	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso homers (30) on a fly ball to left field. Starling Marte scores.

2022-08-19	SI	96.1	2017	Coonrod, Sam(R)	Alonso, Pete(R)	101.1	14°	240	
1-1	Top 9	Hit Into Play	
Pete Alonso doubles (23) on a sharp line drive to left fielder Matt Vierling.

2022-08-19	FF	96.0	2163	Coonrod, Sam(R)	Alonso, Pete(R)	69.2	44°	175	
1-0	Top 9	Foul	
Pete Alonso doubles (23) on a sharp line drive to left fielder Matt Vierling.

2022-08-19	SI	93.4	2299	Nola, Aaron(R)	Alonso, Pete(R)	82.0	-10°	14	
1-2	Top 1	Hit Into Play	
Pete Alonso reaches on a fielder's choice, fielded by third baseman Alec Bohm. Brandon Nimmo scores. Francisco Lindor to 3rd. Throwing error by third baseman Alec Bohm.

2022-08-19	FF	94.9	2266	Coonrod, Sam(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso doubles (23) on a sharp line drive to left fielder Matt Vierling.

2022-08-19	KC	81.0	2723	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso reaches on a fielder's choice, fielded by third baseman Alec Bohm. Brandon Nimmo scores. Francisco Lindor to 3rd. Throwing error by third baseman Alec Bohm.

2022-08-19	FF	92.6	2353	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Called Strike	
Pete Alonso reaches on a fielder's choice, fielded by third baseman Alec Bohm. Brandon Nimmo scores. Francisco Lindor to 3rd. Throwing error by third baseman Alec Bohm.

2022-08-19	KC	79.8	2709	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso reaches on a fielder's choice, fielded by third baseman Alec Bohm. Brandon Nimmo scores. Francisco Lindor to 3rd. Throwing error by third baseman Alec Bohm.

2022-08-19	FF	95.2	2470	Bellatti, Andrew(R)	Alonso, Pete(R)	92.7	18°	279	
0-1	Top 7	Hit Into Play	
Pete Alonso lines out to center fielder Bradley Zimmer.

2022-08-19	SL	87.4	2418	Bellatti, Andrew(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Swinging Strike	
Pete Alonso lines out to center fielder Bradley Zimmer.

2022-08-18	SL	88.4	2585	Fried, Max(L)	Alonso, Pete(R)	--	°		
2-2	Top 6	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-08-18	FF	92.1	2092	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-08-18	FF	94.0	2237	Fried, Max(L)	Alonso, Pete(R)	77.0	12°	142	
1-1	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-08-18	FF	93.2	2191	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-08-18	SI	94.0	2139	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-08-18	FF	96.1	2244	Fried, Max(L)	Alonso, Pete(R)	67.6	46°	211	
2-2	Top 4	Hit Into Play	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	SI	94.9	2121	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-2	Top 4	Ball	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	SL	83.1	2770	Fried, Max(L)	Alonso, Pete(R)	60.7	25°	143	
1-2	Top 4	Foul	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	FF	94.5	2175	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-1	Top 4	Called Strike	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	CH	87.7	1412	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-0	Top 4	Swinging Strike	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	CH	87.8	1393	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso flies out to shortstop Dansby Swanson.

2022-08-18	FF	95.1	2191	Fried, Max(L)	Alonso, Pete(R)	83.8	70°	146	
1-1	Top 2	Hit Into Play	
Pete Alonso pops out to first baseman Matt Olson in foul territory.

2022-08-18	ST	83.1	2700	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Top 2	Ball	
Pete Alonso pops out to first baseman Matt Olson in foul territory.

2022-08-18	SL	85.1	2505	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Swinging Strike	
Pete Alonso pops out to first baseman Matt Olson in foul territory.

2022-08-18	SI	92.9	2321	Jansen, Kenley(R)	Alonso, Pete(R)	78.4	53°	207	
0-0	Top 9	Hit Into Play	
Pete Alonso flies into a force out, right fielder Ronald Acuna Jr. to second baseman Vaughn Grissom. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-08-17	FF	93.7	2163	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
2-2	Top 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-17	FS	85.7	1068	Odorizzi, Jake(R)	Alonso, Pete(R)	78.4	-17°	6	
2-2	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-08-17	FC	88.2	2106	Odorizzi, Jake(R)	Alonso, Pete(R)	60.5	-39°	3	
2-2	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-08-17	SL	81.2	2051	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-08-17	FS	85.3	1364	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-08-17	FC	87.8	2097	Odorizzi, Jake(R)	Alonso, Pete(R)	67.3	59°	168	
0-1	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-08-17	FF	92.2	2195	Odorizzi, Jake(R)	Alonso, Pete(R)	73.6	18°	174	
0-0	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-08-17	FS	85.3	1340	Odorizzi, Jake(R)	Alonso, Pete(R)	99.3	40°	330	
1-1	Top 3	Hit Into Play	
Pete Alonso flies out to left fielder Robbie Grossman.

2022-08-17	FS	84.6	1213	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
1-0	Top 3	Swinging Strike	
Pete Alonso flies out to left fielder Robbie Grossman.

2022-08-17	FC	86.8	2098	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso flies out to left fielder Robbie Grossman.

2022-08-17	CU	79.8	3152	Stephens, Jackson(R)	Alonso, Pete(R)	99.3	15°	244	
3-2	Top 9	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	FF	95.2	2170	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Ball	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	SI	95.8	1937	Stephens, Jackson(R)	Alonso, Pete(R)	110.2	-6°	23	
2-1	Top 9	Foul	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	CU	79.9	3092	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Ball	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	SI	95.3	1895	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	SI	94.7	1981	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Foul	
Pete Alonso singles on a line drive to center fielder Michael Harris II. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-17	FF	93.2	2323	Yates, Kirby(R)	Alonso, Pete(R)	61.3	81°	43	
1-1	Top 7	Hit Into Play	
Pete Alonso pops out to catcher William Contreras in foul territory.

2022-08-17	FC	87.4	2152	Odorizzi, Jake(R)	Alonso, Pete(R)	88.0	21°	316	
1-0	Top 1	Hit Into Play	
Pete Alonso lines out to left fielder Robbie Grossman.

2022-08-17	FS	86.3	1234	Yates, Kirby(R)	Alonso, Pete(R)	64.4	-20°	5	
1-0	Top 7	Foul	
Pete Alonso pops out to catcher William Contreras in foul territory.

2022-08-17	FC	86.5	2078	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso lines out to left fielder Robbie Grossman.

2022-08-17	FS	86.9	1391	Yates, Kirby(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso pops out to catcher William Contreras in foul territory.

2022-08-16	CU	81.4	3016	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-2	Top 7	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-08-16	CU	81.2	3046	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-1	Top 7	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-08-16	FF	92.3	2186	Morton, Charlie(R)	Alonso, Pete(R)	75.1	64°	182	
1-0	Top 7	Foul	
Pete Alonso strikes out swinging.

2022-08-16	SI	93.4	2235	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-08-16	SI	94.1	2148	Morton, Charlie(R)	Alonso, Pete(R)	65.7	15°	137	
0-1	Top 4	Hit Into Play	
Pete Alonso lines out to third baseman Austin Riley.

2022-08-16	CU	80.5	3005	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Swinging Strike	
Pete Alonso lines out to third baseman Austin Riley.

2022-08-16	FF	95.3	2411	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
3-2	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-08-16	CU	82.3	3102	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Ball	
Pete Alonso called out on strikes.

2022-08-16	CU	81.3	2983	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-1	Top 2	Swinging Strike	
Pete Alonso called out on strikes.

2022-08-16	SI	95.3	2224	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Ball	
Pete Alonso called out on strikes.

2022-08-16	SI	93.9	2239	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-1	Top 2	Ball	
Pete Alonso called out on strikes.

2022-08-16	FC	88.1	2480	Morton, Charlie(R)	Alonso, Pete(R)	66.3	34°	170	
0-0	Top 2	Foul	
Pete Alonso called out on strikes.

2022-08-15	SL	85.9	2427	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-15	SL	86.6	2381	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-08-15	SL	85.8	2499	Strider, Spencer(R)	Alonso, Pete(R)	72.9	7°	58	
0-1	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-08-15	FF	96.2	2307	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso strikes out swinging.

2022-08-15	SL	86.3	2303	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-15	FF	98.3	2330	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-08-15	FF	98.4	2341	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-0	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-15	FF	97.9	2330	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-08-15	FF	97.9	2297	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-08-15	ST	81.3	3000	McHugh, Collin(R)	Alonso, Pete(R)	85.0	1°	47	
1-1	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Austin Riley to first baseman Matt Olson.

2022-08-15	ST	81.5	2937	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Swinging Strike	
Pete Alonso grounds out, third baseman Austin Riley to first baseman Matt Olson.

2022-08-15	FC	91.4	2637	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out, third baseman Austin Riley to first baseman Matt Olson.

2022-08-14	SL	89.7	2442	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-14	CU	81.7	2672	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-14	FF	95.7	2497	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-14	SI	95.7	2235	Wheeler, Zack(R)	Alonso, Pete(R)	105.9	-1°	35	
0-0	Bot 4	Hit Into Play	
Pete Alonso doubles (22) on a sharp ground ball to left fielder Matt Vierling.

2022-08-14	SI	96.8	2397	Wheeler, Zack(R)	Alonso, Pete(R)	93.2	40°	332	
0-2	Bot 1	Hit Into Play	
Pete Alonso flies out to center fielder Brandon Marsh.

2022-08-14	SI	96.8	2194	Wheeler, Zack(R)	Alonso, Pete(R)	57.9	67°	107	
0-1	Bot 1	Foul	
Pete Alonso flies out to center fielder Brandon Marsh.

2022-08-14	FF	97.4	2451	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Foul	
Pete Alonso flies out to center fielder Brandon Marsh.

2022-08-14	SL	84.2	2290	Bellatti, Andrew(R)	Alonso, Pete(R)	66.2	-47°	1	
1-2	Bot 7	Hit Into Play	
Pete Alonso grounds into a force out, fielded by third baseman Alec Bohm. Brandon Nimmo out at 3rd. Francisco Lindor to 2nd. Pete Alonso to 1st.

2022-08-14	FF	94.1	2531	Bellatti, Andrew(R)	Alonso, Pete(R)	--	°		
1-1	Bot 7	Called Strike	
Pete Alonso grounds into a force out, fielded by third baseman Alec Bohm. Brandon Nimmo out at 3rd. Francisco Lindor to 2nd. Pete Alonso to 1st.

2022-08-14	FF	94.1	2490	Bellatti, Andrew(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Ball	
Pete Alonso grounds into a force out, fielded by third baseman Alec Bohm. Brandon Nimmo out at 3rd. Francisco Lindor to 2nd. Pete Alonso to 1st.

2022-08-14	SL	84.8	2423	Bellatti, Andrew(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Swinging Strike	
Pete Alonso grounds into a force out, fielded by third baseman Alec Bohm. Brandon Nimmo out at 3rd. Francisco Lindor to 2nd. Pete Alonso to 1st.

2022-08-13	FF	90.8	2212	Nola, Aaron(R)	Alonso, Pete(R)	85.9	60°	193	
1-0	Bot 6	Hit Into Play	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-08-13	FF	93.8	2290	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-08-13	SI	93.2	2230	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-2	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-13	FF	92.0	2380	Nola, Aaron(R)	Alonso, Pete(R)	70.0	59°	182	
0-1	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-13	KC	80.2	2670	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-13	FF	94.7	2384	Nola, Aaron(R)	Alonso, Pete(R)	89.6	22°	265	
0-1	Bot 1	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Starling Marte scores.

2022-08-13	FF	94.6	2352	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Starling Marte scores.

2022-08-12	FC	92.0	1930	Suárez, Ranger(L)	Alonso, Pete(R)	66.5	-9°	13	
2-1	Bot 7	Hit Into Play	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-12	FF	92.9	1937	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
1-1	Bot 7	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-12	FF	91.8	1930	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Swinging Strike	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-12	CU	76.5	2260	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-08-12	SI	94.1	1950	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
2-2	Bot 4	Called Strike	
Pete Alonso called out on strikes.

2022-08-12	CU	77.2	2236	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Blocked Ball	
Pete Alonso called out on strikes.

2022-08-12	SI	92.6	1909	Suárez, Ranger(L)	Alonso, Pete(R)	71.4	34°	197	
1-1	Bot 4	Foul	
Pete Alonso called out on strikes.

2022-08-12	FF	94.5	2037	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Swinging Strike	
Pete Alonso called out on strikes.

2022-08-12	SI	93.6	2027	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso called out on strikes.

2022-08-12	FF	94.5	1926	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
3-2	Bot 2	Ball	
Pete Alonso walks.

2022-08-12	FF	91.9	1897	Suárez, Ranger(L)	Alonso, Pete(R)	78.7	67°	190	
3-1	Bot 2	Foul	
Pete Alonso walks.

2022-08-12	CH	82.6	1226	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
2-1	Bot 2	Ball	
Pete Alonso walks.

2022-08-12	SI	93.1	1897	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
2-0	Bot 2	Called Strike	
Pete Alonso walks.

2022-08-12	FF	90.5	1934	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
1-0	Bot 2	Ball	
Pete Alonso walks.

2022-08-12	SI	92.2	1829	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso walks.

2022-08-10	SL	78.8	1976	Zeuch, T.J.(R)	Alonso, Pete(R)	79.4	-5°	15	
1-1	Bot 4	Hit Into Play	
Pete Alonso grounds into a double play, third baseman Donovan Solano to second baseman Jonathan India to first baseman Joey Votto. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-10	FC	86.3	2022	Zeuch, T.J.(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Foul	
Pete Alonso grounds into a double play, third baseman Donovan Solano to second baseman Jonathan India to first baseman Joey Votto. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-10	SL	79.3	1912	Zeuch, T.J.(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso grounds into a double play, third baseman Donovan Solano to second baseman Jonathan India to first baseman Joey Votto. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-08-10	SI	90.3	2069	Zeuch, T.J.(R)	Alonso, Pete(R)	105.4	11°	220	
0-0	Bot 2	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Jake Fraley. Francisco Lindor to 2nd.

2022-08-10	SI	92.0	2249	Zeuch, T.J.(R)	Alonso, Pete(R)	100.6	-7°	13	
0-1	Bot 1	Hit Into Play	
Pete Alonso singles on a ground ball to center fielder Nick Senzel. Brandon Nimmo scores. Francisco Lindor to 3rd. Pete Alonso to 2nd.

2022-08-10	SL	80.6	2083	Zeuch, T.J.(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso singles on a ground ball to center fielder Nick Senzel. Brandon Nimmo scores. Francisco Lindor to 3rd. Pete Alonso to 2nd.

2022-08-10	ST	82.9	2450	Gibaut, Ian(R)	Alonso, Pete(R)	100.0	10°	192	
1-2	Bot 6	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Jake Fraley. Brandon Nimmo to 3rd. Francisco Lindor to 2nd.

2022-08-10	SI	92.3	2007	Strickland, Hunter(R)	Alonso, Pete(R)	110.1	-3°	25	
0-0	Bot 8	Hit Into Play	
Pete Alonso grounds out sharply, shortstop Jose Barrero to first baseman Matt Reynolds.

2022-08-10	CH	84.5	1601	Gibaut, Ian(R)	Alonso, Pete(R)	75.0	55°	234	
1-1	Bot 6	Foul	
Pete Alonso singles on a line drive to left fielder Jake Fraley. Brandon Nimmo to 3rd. Francisco Lindor to 2nd.

2022-08-10	FF	94.0	2186	Gibaut, Ian(R)	Alonso, Pete(R)	63.8	36°	168	
1-0	Bot 6	Foul	
Pete Alonso singles on a line drive to left fielder Jake Fraley. Brandon Nimmo to 3rd. Francisco Lindor to 2nd.

2022-08-10	FF	94.9	2207	Gibaut, Ian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso singles on a line drive to left fielder Jake Fraley. Brandon Nimmo to 3rd. Francisco Lindor to 2nd.

2022-08-09	FF	90.6	2429	Minor, Mike(L)	Alonso, Pete(R)	59.6	24°	175	
1-2	Bot 6	Hit Into Play	
Pete Alonso lines out to shortstop Jose Barrero.

2022-08-09	KC	79.0	2400	Minor, Mike(L)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Foul Tip	
Pete Alonso lines out to shortstop Jose Barrero.

2022-08-09	FF	90.1	2402	Minor, Mike(L)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Foul Tip	
Pete Alonso lines out to shortstop Jose Barrero.

2022-08-09	KC	77.1	2398	Minor, Mike(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso lines out to shortstop Jose Barrero.

2022-08-09	CH	85.2	2114	Minor, Mike(L)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-09	FF	90.7	2395	Minor, Mike(L)	Alonso, Pete(R)	66.6	27°	189	
3-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	FF	91.0	2353	Minor, Mike(L)	Alonso, Pete(R)	66.4	55°	165	
3-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	KC	80.8	2502	Minor, Mike(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-08-09	FF	90.0	2386	Minor, Mike(L)	Alonso, Pete(R)	98.1	58°	248	
2-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	CH	84.9	2116	Minor, Mike(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	FF	89.9	2435	Minor, Mike(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-08-09	SL	86.4	2682	Minor, Mike(L)	Alonso, Pete(R)	88.0	-10°	10	
1-2	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	FF	90.9	2522	Minor, Mike(L)	Alonso, Pete(R)	61.9	64°	132	
1-1	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-08-09	FF	90.9	2440	Minor, Mike(L)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-08-09	KC	78.9	2410	Minor, Mike(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-08-09	FF	92.1	2581	Minor, Mike(L)	Alonso, Pete(R)	65.2	54°	157	
1-0	Bot 1	Hit Into Play	
Pete Alonso pops out to shortstop Jose Barrero on the infield fly rule.

2022-08-09	FF	91.9	2552	Minor, Mike(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso pops out to shortstop Jose Barrero on the infield fly rule.

2022-08-08	SL	83.1	2356	Dunn, Justin(R)	Alonso, Pete(R)	70.9	65°	131	
0-0	Bot 5	Hit Into Play	
Pete Alonso pops out to third baseman Nick Senzel in foul territory.

2022-08-08	SL	82.9	2398	Dunn, Justin(R)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-08-08	FF	93.1	2176	Dunn, Justin(R)	Alonso, Pete(R)	82.7	26°	251	
1-2	Bot 3	Foul	
Pete Alonso strikes out swinging.

2022-08-08	CU	78.5	2220	Dunn, Justin(R)	Alonso, Pete(R)	74.6	78°	107	
1-1	Bot 3	Foul	
Pete Alonso strikes out swinging.

2022-08-08	FF	92.1	2114	Dunn, Justin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-08	FF	91.6	2093	Dunn, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso strikes out swinging.

2022-08-08	SL	83.0	2349	Dunn, Justin(R)	Alonso, Pete(R)	98.0	21°	345	
0-0	Bot 1	Hit Into Play	
Pete Alonso lines out to center fielder Nick Senzel.

2022-08-08	SL	86.2	2377	Hendrix, Ryan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-08-08	SL	85.1	2220	Hendrix, Ryan(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Swinging Strike	
Pete Alonso strikes out on a foul tip.

2022-08-08	SI	96.2	2125	Hendrix, Ryan(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso strikes out on a foul tip.

2022-08-08	FF	95.6	2192	Hendrix, Ryan(R)	Alonso, Pete(R)	76.5	46°	217	
1-0	Bot 8	Foul	
Pete Alonso strikes out on a foul tip.

2022-08-08	FF	95.7	2120	Hendrix, Ryan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso strikes out on a foul tip.

2022-08-07	SL	86.0	2418	Strider, Spencer(R)	Alonso, Pete(R)	80.5	-1°	24	
2-2	Bot 3	Hit Into Play	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	SL	87.6	2344	Strider, Spencer(R)	Alonso, Pete(R)	43.4	-37°	2	
2-2	Bot 3	Foul	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FF	98.9	2344	Strider, Spencer(R)	Alonso, Pete(R)	57.0	50°	146	
2-2	Bot 3	Foul	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FF	99.8	2366	Strider, Spencer(R)	Alonso, Pete(R)	74.6	37°	212	
2-2	Bot 3	Foul	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	SL	89.5	2438	Strider, Spencer(R)	Alonso, Pete(R)	63.7	-35°	1	
2-1	Bot 3	Foul	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FF	100.1	2284	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FF	99.1	2320	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FF	99.5	2300	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Swinging Strike	
Pete Alonso doubles (21) on a ground ball to left fielder Eddie Rosario. Brandon Nimmo scores. Francisco Lindor scores.

2022-08-07	FC	90.9	2553	McHugh, Collin(R)	Alonso, Pete(R)	78.6	27°	267	
1-1	Bot 6	Hit Into Play	
Pete Alonso lines out to right fielder Robbie Grossman.

2022-08-07	FC	91.3	2558	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Swinging Strike	
Pete Alonso lines out to right fielder Robbie Grossman.

2022-08-07	ST	83.3	2742	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso lines out to right fielder Robbie Grossman.

2022-08-07	SL	89.1	2198	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-07	FF	99.6	2184	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-08-07	SL	89.1	2286	Strider, Spencer(R)	Alonso, Pete(R)	71.3	26°	216	
2-2	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-08-07	SL	88.9	2274	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-08-07	FF	99.8	2283	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-08-07	SL	88.5	2296	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Blocked Ball	
Pete Alonso strikes out swinging.

2022-08-07	SL	90.4	2305	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-06	FF	92.0	2005	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Called Strike	
Pete Alonso called out on strikes.

2022-08-06	FS	86.2	1334	Odorizzi, Jake(R)	Alonso, Pete(R)	112.6	17°	295	
2-1	Bot 5	Foul	
Pete Alonso called out on strikes.

2022-08-06	FC	86.0	1987	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso called out on strikes.

2022-08-06	SL	82.4	2008	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Ball	
Pete Alonso called out on strikes.

2022-08-06	FC	86.5	2121	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Foul	
Pete Alonso called out on strikes.

2022-08-06	CH	88.2	1370	Fried, Max(L)	Alonso, Pete(R)	56.5	-48°	1	
1-2	Bot 6	Hit Into Play	
Pete Alonso singles on a soft ground ball to pitcher Max Fried.

2022-08-06	CU	73.5	2738	Fried, Max(L)	Alonso, Pete(R)	81.4	-19°	5	
1-1	Bot 6	Foul	
Pete Alonso singles on a soft ground ball to pitcher Max Fried.

2022-08-06	CH	86.4	1296	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Swinging Strike	
Pete Alonso singles on a soft ground ball to pitcher Max Fried.

2022-08-06	SI	92.5	1877	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso singles on a soft ground ball to pitcher Max Fried.

2022-08-06	FS	84.8	1131	Odorizzi, Jake(R)	Alonso, Pete(R)	79.0	44°	265	
1-0	Bot 3	Hit Into Play	
Pete Alonso flies out to left fielder Robbie Grossman.

2022-08-06	FS	85.2	1253	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso flies out to left fielder Robbie Grossman.

2022-08-06	FF	97.1	2220	Fried, Max(L)	Alonso, Pete(R)	72.3	32°	229	
0-0	Bot 3	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Ronald Acuna Jr. Tomas Nido scores. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-08-06	SI	93.1	2088	Elder, Bryce(R)	Alonso, Pete(R)	101.7	39°	358	
0-2	Bot 7	Hit Into Play	
Pete Alonso flies out sharply to left fielder Robbie Grossman.

2022-08-06	SL	83.4	2395	Elder, Bryce(R)	Alonso, Pete(R)	72.0	68°	113	
0-1	Bot 7	Foul	
Pete Alonso flies out sharply to left fielder Robbie Grossman.

2022-08-06	SI	92.1	2029	Elder, Bryce(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Swinging Strike	
Pete Alonso flies out sharply to left fielder Robbie Grossman.

2022-08-06	FC	87.8	1983	Odorizzi, Jake(R)	Alonso, Pete(R)	79.9	16°	203	
1-0	Bot 1	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Starling Marte scores. Francisco Lindor to 3rd.

2022-08-06	CU	75.6	2923	Fried, Max(L)	Alonso, Pete(R)	84.5	17°	230	
1-2	Bot 1	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Eddie Rosario. Francisco Lindor to 2nd.

2022-08-06	FF	92.6	1996	Odorizzi, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Starling Marte scores. Francisco Lindor to 3rd.

2022-08-06	FF	93.8	2284	Fried, Max(L)	Alonso, Pete(R)	73.3	36°	194	
1-1	Bot 1	Foul	
Pete Alonso singles on a line drive to left fielder Eddie Rosario. Francisco Lindor to 2nd.

2022-08-06	CU	77.8	3062	Stephens, Jackson(R)	Alonso, Pete(R)	72.3	-7°	16	
1-1	Bot 7	Hit Into Play	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-08-06	SI	95.6	1961	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Ball	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-08-06	FF	92.7	2179	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Swinging Strike	
Pete Alonso singles on a line drive to left fielder Eddie Rosario. Francisco Lindor to 2nd.

2022-08-06	FF	94.7	2064	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-08-06	FF	94.3	2077	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso singles on a line drive to left fielder Eddie Rosario. Francisco Lindor to 2nd.

2022-08-05	FF	93.7	2126	Anderson, Ian(R)	Alonso, Pete(R)	100.3	10°	198	
2-0	Bot 5	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Eddie Rosario. Francisco Lindor to 3rd.

2022-08-05	CH	87.1	1552	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Pete Alonso singles on a sharp line drive to left fielder Eddie Rosario. Francisco Lindor to 3rd.

2022-08-05	FF	91.9	2103	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a sharp line drive to left fielder Eddie Rosario. Francisco Lindor to 3rd.

2022-08-05	FF	94.7	2150	Anderson, Ian(R)	Alonso, Pete(R)	111.2	15°	332	
0-0	Bot 3	Hit Into Play	
Pete Alonso lines out sharply to right fielder Ronald Acuna Jr.

2022-08-05	FF	94.5	2112	Anderson, Ian(R)	Alonso, Pete(R)	102.6	30°	370	
3-2	Bot 1	Hit Into Play	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	ST	81.1	2844	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
3-2	Bot 6	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	FF	94.1	2166	Anderson, Ian(R)	Alonso, Pete(R)	75.0	40°	217	
3-1	Bot 1	Foul	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	ST	81.6	2744	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
2-2	Bot 6	Blocked Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	CH	88.4	1374	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Blocked Ball	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	ST	80.5	2681	McHugh, Collin(R)	Alonso, Pete(R)	50.3	34°	119	
2-2	Bot 6	Foul	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	ST	81.0	2676	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	FF	94.5	2139	Anderson, Ian(R)	Alonso, Pete(R)	81.1	81°	63	
2-0	Bot 1	Foul	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	ST	81.0	2730	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Swinging Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	FF	94.1	2197	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	FF	94.2	2117	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out sharply to right fielder Ronald Acuna Jr.

2022-08-05	FC	91.5	2635	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Foul	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	FC	91.6	2585	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-08-05	SI	94.0	2114	Jansen, Kenley(R)	Alonso, Pete(R)	--	°		
1-2	Bot 9	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-08-05	FC	91.5	2646	Jansen, Kenley(R)	Alonso, Pete(R)	88.6	36°	298	
1-1	Bot 9	Foul	
Pete Alonso strikes out on a foul tip.

2022-08-05	FC	91.8	2604	Jansen, Kenley(R)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-08-05	FC	91.8	2643	Jansen, Kenley(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Ball	
Pete Alonso strikes out on a foul tip.

2022-08-04	SI	92.4	2237	Wright, Kyle(R)	Alonso, Pete(R)	96.7	-20°	5	
0-0	Bot 5	Hit Into Play	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson.

2022-08-04	KC	85.5	2878	Wright, Kyle(R)	Alonso, Pete(R)	109.5	19°	412	
1-1	Bot 3	Hit Into Play	
Pete Alonso homers (29) on a fly ball to left center field. Francisco Lindor scores.

2022-08-04	KC	84.8	2811	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso homers (29) on a fly ball to left center field. Francisco Lindor scores.

2022-08-04	SI	93.4	2338	Wright, Kyle(R)	Alonso, Pete(R)	84.1	86°	73	
0-0	Bot 3	Foul	
Pete Alonso homers (29) on a fly ball to left center field. Francisco Lindor scores.

2022-08-04	KC	85.9	2731	Wright, Kyle(R)	Alonso, Pete(R)	100.6	12°	224	
0-0	Bot 1	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Eddie Rosario. Starling Marte scores. Francisco Lindor to 3rd.

2022-08-04	SI	95.5	2006	Stephens, Jackson(R)	Alonso, Pete(R)	84.4	-30°	4	
0-0	Bot 8	Hit Into Play	
Pete Alonso grounds out, second baseman Orlando Arcia to first baseman Matt Olson.

2022-08-03	SL	81.9	2176	Sánchez, Aníbal(R)	Alonso, Pete(R)	103.0	25°	411	
0-0	Top 3	Hit Into Play	
Pete Alonso homers (28) on a fly ball to center field. Francisco Lindor scores.

2022-08-03	SL	87.3	2218	Weems, Jordan(R)	Alonso, Pete(R)	98.5	52°	261	
2-0	Top 6	Hit Into Play	
Pete Alonso flies out to center fielder Victor Robles.

2022-08-03	FF	95.1	2098	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-08-03	FF	96.3	2053	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-08-03	FF	97.3	2160	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-2	Top 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-03	SI	90.2	1873	Sánchez, Aníbal(R)	Alonso, Pete(R)	89.0	29°	321	
3-2	Top 1	Hit Into Play	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	SL	88.9	1948	Machado, Andrés(R)	Alonso, Pete(R)	67.4	-4°	17	
0-2	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-08-03	SI	97.4	2182	Machado, Andrés(R)	Alonso, Pete(R)	62.0	-4°	23	
0-2	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-08-03	FC	89.0	2093	Sánchez, Aníbal(R)	Alonso, Pete(R)	100.2	47°	331	
3-2	Top 1	Foul	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	FF	97.7	2163	Machado, Andrés(R)	Alonso, Pete(R)	86.9	56°	232	
0-2	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-08-03	SI	91.8	1975	Sánchez, Aníbal(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Ball	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	SI	96.2	2141	Machado, Andrés(R)	Alonso, Pete(R)	77.7	27°	233	
0-1	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-08-03	SI	91.9	1989	Sánchez, Aníbal(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	FC	88.8	2183	Sánchez, Aníbal(R)	Alonso, Pete(R)	81.5	38°	274	
1-1	Top 1	Foul	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	SI	96.6	2086	Machado, Andrés(R)	Alonso, Pete(R)	66.8	47°	185	
0-0	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-08-03	FF	91.0	2147	Sánchez, Aníbal(R)	Alonso, Pete(R)	89.5	57°	219	
1-0	Top 1	Foul	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-03	SI	89.1	1952	Sánchez, Aníbal(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso flies out to right fielder Josh Palacios.

2022-08-02	SL	87.7	2171	Abbott, Cory(R)	Alonso, Pete(R)	60.8	-49°	2	
0-0	Top 3	Hit Into Play	
Pete Alonso grounds out to first baseman Joey Meneses.

2022-08-02	SL	87.8	2162	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-02	FF	93.8	2382	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-08-02	SL	88.3	2139	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-08-02	SL	87.4	2130	Abbott, Cory(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-08-02	FF	92.7	2290	Abbott, Cory(R)	Alonso, Pete(R)	82.6	67°	191	
0-0	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-08-02	SL	92.9	2204	Finnegan, Kyle(R)	Alonso, Pete(R)	83.2	27°	312	
0-1	Top 8	Hit Into Play	
Pete Alonso lines out to center fielder Victor Robles.

2022-08-02	SI	97.6	1852	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso lines out to center fielder Victor Robles.

2022-08-02	SL	82.5	2582	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-08-02	SL	85.5	2574	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Called Strike	
Pete Alonso strikes out swinging.

2022-08-02	SI	95.1	2237	Arano, Víctor(R)	Alonso, Pete(R)	85.8	-31°	3	
0-0	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-08-01	SL	81.3	2234	Corbin, Patrick(L)	Alonso, Pete(R)	110.9	17°	390	
0-0	Top 3	Hit Into Play	
Pete Alonso homers (27) on a line drive to left center field.

2022-08-01	SL	85.0	2378	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
3-2	Top 2	Ball	
Pete Alonso walks.

2022-08-01	FF	94.1	2238	Corbin, Patrick(L)	Alonso, Pete(R)	80.6	10°	137	
3-2	Top 2	Foul	
Pete Alonso walks.

2022-08-01	SI	94.3	2073	Corbin, Patrick(L)	Alonso, Pete(R)	77.4	35°	222	
3-2	Top 2	Foul	
Pete Alonso walks.

2022-08-01	SI	94.6	2204	Corbin, Patrick(L)	Alonso, Pete(R)	77.1	14°	168	
3-1	Top 2	Foul	
Pete Alonso walks.

2022-08-01	SI	93.9	2083	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
3-0	Top 2	Called Strike	
Pete Alonso walks.

2022-08-01	SI	92.4	2093	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-0	Top 2	Ball	
Pete Alonso walks.

2022-08-01	FF	92.3	2237	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso walks.

2022-08-01	FF	88.5	2449	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
3-1	Top 6	Ball	
Pete Alonso walks.

2022-08-01	FF	87.9	2396	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
3-0	Top 6	Called Strike	
Pete Alonso walks.

2022-08-01	SI	93.1	2078	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso walks.

2022-08-01	FF	89.3	2426	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
2-0	Top 6	Ball	
Pete Alonso walks.

2022-08-01	SL	77.5	2258	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso walks.

2022-08-01	SL	77.4	2244	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso walks.

2022-08-01	FF	98.5	1990	Harvey, Hunter(R)	Alonso, Pete(R)	102.8	36°	385	
3-2	Top 9	Hit Into Play	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	FF	96.4	2033	Machado, Andrés(R)	Alonso, Pete(R)	78.1	40°	246	
1-2	Top 5	Hit Into Play	
Pete Alonso hits a ground-rule double (20) on a fly ball down the right-field line.

2022-08-01	FF	98.2	1894	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Ball	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	FF	97.9	1821	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	SL	88.9	2009	Machado, Andrés(R)	Alonso, Pete(R)	60.0	70°	108	
1-2	Top 5	Foul	
Pete Alonso hits a ground-rule double (20) on a fly ball down the right-field line.

2022-08-01	FF	98.1	1929	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Swinging Strike	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	SL	88.4	2056	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso hits a ground-rule double (20) on a fly ball down the right-field line.

2022-08-01	SI	96.0	2084	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Called Strike	
Pete Alonso hits a ground-rule double (20) on a fly ball down the right-field line.

2022-08-01	FF	97.9	1918	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Foul	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	FF	98.4	1970	Harvey, Hunter(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso flies out sharply to center fielder Victor Robles.

2022-08-01	SI	94.6	1986	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Foul	
Pete Alonso hits a ground-rule double (20) on a fly ball down the right-field line.

2022-07-31	SI	94.7	2105	López, Pablo(R)	Alonso, Pete(R)	71.7	0°	46	
3-2	Top 2	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	CU	81.2	2558	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Blocked Ball	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	CH	88.0	2082	López, Pablo(R)	Alonso, Pete(R)	106.4	-21°	5	
2-2	Top 2	Foul	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	SI	95.2	2043	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-1	Top 2	Foul	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	CH	88.0	2073	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Ball	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	CH	88.2	2076	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Swinging Strike	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	SL	72.8	2312	Fishman, Jake(L)	Alonso, Pete(R)	76.1	51°	216	
0-1	Top 5	Hit Into Play	
Pete Alonso pops out to shortstop Miguel Rojas.

2022-07-31	CH	89.1	2121	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso grounds into a double play, shortstop Miguel Rojas to second baseman Joey Wendle to first baseman Lewin Diaz. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-31	SI	87.0	1814	Fishman, Jake(L)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso pops out to shortstop Miguel Rojas.

2022-07-31	FF	93.1	1890	Brigham, Jeff(R)	Alonso, Pete(R)	93.8	42°	315	
1-1	Top 7	Hit Into Play	
Pete Alonso flies out to left fielder Jesus Sanchez.

2022-07-31	FF	94.6	2339	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Ball	
Pete Alonso flies out to left fielder Jesus Sanchez.

2022-07-31	ST	81.6	2591	Brigham, Jeff(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso flies out to left fielder Jesus Sanchez.

2022-07-31	FF	96.0	2138	López, Pablo(R)	Alonso, Pete(R)	107.8	17°	325	
1-1	Top 1	Hit Into Play	
Pete Alonso doubles (19) on a sharp line drive to right fielder Bryan De La Cruz. Francisco Lindor scores.

2022-07-31	FF	96.3	2203	López, Pablo(R)	Alonso, Pete(R)	83.0	48°	232	
1-0	Top 1	Foul	
Pete Alonso doubles (19) on a sharp line drive to right fielder Bryan De La Cruz. Francisco Lindor scores.

2022-07-31	CH	87.5	1855	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso doubles (19) on a sharp line drive to right fielder Bryan De La Cruz. Francisco Lindor scores.

2022-07-31	SI	88.6	1992	Fishman, Jake(L)	Alonso, Pete(R)	111.9	0°	41	
1-2	Top 4	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Bryan De La Cruz.

2022-07-31	SI	88.5	2151	Fishman, Jake(L)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso singles on a ground ball to right fielder Bryan De La Cruz.

2022-07-31	SL	75.0	2380	Fishman, Jake(L)	Alonso, Pete(R)	69.6	59°	158	
0-1	Top 4	Foul	
Pete Alonso singles on a ground ball to right fielder Bryan De La Cruz.

2022-07-31	SL	73.3	2207	Fishman, Jake(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso singles on a ground ball to right fielder Bryan De La Cruz.

2022-07-30	SL	86.5	2205	Neidert, Nick(R)	Alonso, Pete(R)	91.4	31°	320	
3-2	Top 3	Hit Into Play	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	SL	87.5	2170	Neidert, Nick(R)	Alonso, Pete(R)	--	°		
2-2	Top 3	Blocked Ball	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	FF	91.9	2187	Neidert, Nick(R)	Alonso, Pete(R)	73.5	8°	105	
2-2	Top 3	Foul	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	CH	84.7	1571	Neidert, Nick(R)	Alonso, Pete(R)	86.8	58°	205	
2-2	Top 3	Foul	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	SL	86.5	2166	Neidert, Nick(R)	Alonso, Pete(R)	71.3	41°	188	
2-1	Top 3	Foul	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	FF	91.6	2214	Neidert, Nick(R)	Alonso, Pete(R)	64.8	39°	166	
2-0	Top 3	Foul	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	CH	84.4	1642	Neidert, Nick(R)	Alonso, Pete(R)	--	°		
1-0	Top 3	Ball	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	FF	90.6	2178	Neidert, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-07-30	CH	89.3	1835	Brazoban, Huascar(R)	Alonso, Pete(R)	69.7	-21°	4	
2-0	Top 8	Hit Into Play	
Pete Alonso grounds out, pitcher Huascar Brazoban to first baseman Lewin Diaz.

2022-07-30	SI	96.6	2229	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso grounds out, pitcher Huascar Brazoban to first baseman Lewin Diaz.

2022-07-30	SI	97.5	2338	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso grounds out, pitcher Huascar Brazoban to first baseman Lewin Diaz.

2022-07-30	FF	91.0	2182	Neidert, Nick(R)	Alonso, Pete(R)	107.4	3°	77	
0-0	Top 2	Hit Into Play	
Pete Alonso grounds out, second baseman Joey Wendle to first baseman Lewin Diaz.

2022-07-30	FC	86.6	2410	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-30	FC	86.5	2455	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-30	SI	96.8	2313	Brazoban, Huascar(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso strikes out swinging.

2022-07-29	SI	99.4	2295	Alcantara, Sandy(R)	Alonso, Pete(R)	97.0	-37°	3	
2-2	Top 5	Hit Into Play	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	CH	91.7	1936	Alcantara, Sandy(R)	Alonso, Pete(R)	91.6	-16°	7	
2-2	Top 5	Foul	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	CH	91.3	2098	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Ball	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	FF	98.2	2063	Alcantara, Sandy(R)	Alonso, Pete(R)	80.5	19°	207	
1-2	Top 5	Foul	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	SL	92.0	2367	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	FF	96.9	2083	Alcantara, Sandy(R)	Alonso, Pete(R)	79.8	22°	224	
0-2	Top 5	Foul	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	SI	96.4	2254	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Foul	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	SL	87.4	2262	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso grounds out, first baseman Lewin Diaz to pitcher Sandy Alcantara.

2022-07-29	SI	97.7	2295	Alcantara, Sandy(R)	Alonso, Pete(R)	92.0	-17°	7	
0-0	Top 2	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Miguel Rojas to second baseman Luke Williams. Francisco Lindor out at 2nd.

2022-07-29	SL	91.9	2324	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-29	SL	91.2	2440	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-07-29	CH	91.4	2060	Alcantara, Sandy(R)	Alonso, Pete(R)	103.3	30°	353	
1-1	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-07-29	SI	97.4	2207	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-07-29	FF	98.2	2220	Alcantara, Sandy(R)	Alonso, Pete(R)	80.5	32°	262	
0-0	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-07-29	SI	95.8	2054	Bass, Anthony(R)	Alonso, Pete(R)	107.0	-15°	5	
0-1	Top 7	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Miguel Rojas to second baseman Luke Williams. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-29	SI	94.4	2025	Bass, Anthony(R)	Alonso, Pete(R)	78.5	-45°	2	
0-0	Top 7	Foul	
Pete Alonso grounds into a force out, shortstop Miguel Rojas to second baseman Luke Williams. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-27	FF	93.1	2504	Germán, Domingo(R)	Alonso, Pete(R)	75.8	81°	49	
1-0	Bot 3	Hit Into Play	
Pete Alonso pops out to first baseman DJ LeMahieu in foul territory.

2022-07-27	SI	93.3	2424	Germán, Domingo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso pops out to first baseman DJ LeMahieu in foul territory.

2022-07-27	CU	81.7	2665	Germán, Domingo(R)	Alonso, Pete(R)	97.0	25°	369	
1-1	Bot 2	Hit Into Play	
Pete Alonso homers (26) on a fly ball to left field.

2022-07-27	SI	94.4	2202	Germán, Domingo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Ball	
Pete Alonso homers (26) on a fly ball to left field.

2022-07-27	FF	93.5	2555	Germán, Domingo(R)	Alonso, Pete(R)	69.2	30°	177	
0-0	Bot 2	Foul	
Pete Alonso homers (26) on a fly ball to left field.

2022-07-27	FC	88.2	2496	Luetge, Lucas(L)	Alonso, Pete(R)	--	°		
3-1	Bot 5	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-27	FC	88.0	2604	Luetge, Lucas(L)	Alonso, Pete(R)	--	°		
3-0	Bot 5	Called Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-27	ST	86.0	2608	Holmes, Clay(R)	Alonso, Pete(R)	85.6	-21°	9	
1-2	Bot 8	Hit Into Play	
Pete Alonso grounds out, pitcher Clay Holmes to first baseman DJ LeMahieu.

2022-07-27	FC	88.2	2553	Luetge, Lucas(L)	Alonso, Pete(R)	--	°		
2-0	Bot 5	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-27	SI	97.3	2213	Holmes, Clay(R)	Alonso, Pete(R)	76.8	-32°	2	
1-1	Bot 8	Foul	
Pete Alonso grounds out, pitcher Clay Holmes to first baseman DJ LeMahieu.

2022-07-27	SI	98.2	2170	Holmes, Clay(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso grounds out, pitcher Clay Holmes to first baseman DJ LeMahieu.

2022-07-27	FC	88.0	2605	Luetge, Lucas(L)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-27	CU	72.3	2435	Luetge, Lucas(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Blocked Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-27	SI	96.7	2088	Holmes, Clay(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso grounds out, pitcher Clay Holmes to first baseman DJ LeMahieu.

2022-07-26	FC	89.8	2486	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Ball	
Pete Alonso walks.

2022-07-26	SI	93.4	2228	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Ball	
Pete Alonso walks.

2022-07-26	CU	81.0	2424	Montgomery, Jordan(L)	Alonso, Pete(R)	73.5	40°	199	
2-2	Bot 3	Foul	
Pete Alonso walks.

2022-07-26	SI	93.1	2314	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso walks.

2022-07-26	CU	78.9	2223	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Swinging Strike	
Pete Alonso walks.

2022-07-26	SI	92.5	2326	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Called Strike	
Pete Alonso walks.

2022-07-26	FC	87.9	2390	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso walks.

2022-07-26	CH	80.8	1644	Montgomery, Jordan(L)	Alonso, Pete(R)	107.1	12°	292	
3-1	Bot 1	Hit Into Play	
Pete Alonso doubles (18) on a sharp line drive to center fielder Aaron Judge. Francisco Lindor scores.

2022-07-26	FC	87.7	2401	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso doubles (18) on a sharp line drive to center fielder Aaron Judge. Francisco Lindor scores.

2022-07-26	CH	81.4	1748	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Called Strike	
Pete Alonso doubles (18) on a sharp line drive to center fielder Aaron Judge. Francisco Lindor scores.

2022-07-26	CU	77.5	2187	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso doubles (18) on a sharp line drive to center fielder Aaron Judge. Francisco Lindor scores.

2022-07-26	CU	77.9	2229	Montgomery, Jordan(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso doubles (18) on a sharp line drive to center fielder Aaron Judge. Francisco Lindor scores.

2022-07-26	SI	98.2	2348	Loáisiga, Jonathan(R)	Alonso, Pete(R)	101.8	12°	246	
2-1	Bot 5	Hit Into Play	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge.

2022-07-26	SI	98.5	2352	Loáisiga, Jonathan(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge.

2022-07-26	SI	97.8	2346	Loáisiga, Jonathan(R)	Alonso, Pete(R)	66.2	55°	159	
1-0	Bot 5	Foul	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge.

2022-07-26	SI	98.1	2355	Loáisiga, Jonathan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge.

2022-07-26	SI	99.2	2231	Abreu, Albert(R)	Alonso, Pete(R)	101.9	9°	185	
0-1	Bot 8	Hit Into Play	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge. Francisco Lindor to 2nd.

2022-07-26	SI	99.7	2295	Abreu, Albert(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso singles on a sharp line drive to center fielder Aaron Judge. Francisco Lindor to 2nd.

2022-07-24	SL	84.8	2684	Musgrove, Joe(R)	Alonso, Pete(R)	109.3	23°	425	
2-1	Bot 6	Hit Into Play	
Pete Alonso homers (25) on a fly ball to center field. Starling Marte scores. Francisco Lindor scores.

2022-07-24	SL	86.4	2793	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Ball	
Pete Alonso homers (25) on a fly ball to center field. Starling Marte scores. Francisco Lindor scores.

2022-07-24	SI	93.6	2442	Musgrove, Joe(R)	Alonso, Pete(R)	38.7	-55°	2	
1-0	Bot 6	Foul	
Pete Alonso homers (25) on a fly ball to center field. Starling Marte scores. Francisco Lindor scores.

2022-07-24	FF	93.5	2631	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso homers (25) on a fly ball to center field. Starling Marte scores. Francisco Lindor scores.

2022-07-24	FC	91.4	2599	Musgrove, Joe(R)	Alonso, Pete(R)	99.4	23°	368	
1-0	Bot 4	Hit Into Play	
Pete Alonso lines out to center fielder Esteury Ruiz.

2022-07-24	CU	81.2	2627	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso lines out to center fielder Esteury Ruiz.

2022-07-24	SL	86.1	2743	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
3-2	Bot 2	Ball	
Pete Alonso walks.

2022-07-24	SL	84.9	2589	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
2-2	Bot 2	Ball	
Pete Alonso walks.

2022-07-24	SL	84.7	2677	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
2-2	Bot 2	Foul	
Pete Alonso walks.

2022-07-24	SL	83.3	2499	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
2-1	Bot 2	Swinging Strike	
Pete Alonso walks.

2022-07-24	SL	84.8	2584	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
1-1	Bot 2	Ball	
Pete Alonso walks.

2022-07-24	FF	92.8	2536	Musgrove, Joe(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Ball	
Pete Alonso walks.

2022-07-24	FC	90.0	2560	Musgrove, Joe(R)	Alonso, Pete(R)	82.9	46°	248	
0-0	Bot 2	Foul	
Pete Alonso walks.

2022-07-24	ST	80.6	2600	Wilson, Steven(R)	Alonso, Pete(R)	102.5	32°	393	
0-0	Bot 7	Hit Into Play	
Pete Alonso doubles (17) on a sharp fly ball to right fielder Nomar Mazara. Starling Marte scores. Francisco Lindor to 3rd.

2022-07-23	SL	87.8	2355	Snell, Blake(L)	Alonso, Pete(R)	98.7	14°	199	
1-0	Bot 4	Hit Into Play	
Pete Alonso doubles (16) on a line drive to left fielder Jurickson Profar.

2022-07-23	FF	95.5	2543	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso doubles (16) on a line drive to left fielder Jurickson Profar.

2022-07-23	FF	96.0	2508	Snell, Blake(L)	Alonso, Pete(R)	89.5	9°	167	
2-1	Bot 2	Hit Into Play	
Pete Alonso singles on a line drive to left fielder Jurickson Profar.

2022-07-23	SL	88.1	2426	Snell, Blake(L)	Alonso, Pete(R)	--	°		
1-1	Bot 2	Ball	
Pete Alonso singles on a line drive to left fielder Jurickson Profar.

2022-07-23	SL	88.5	2497	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Ball	
Pete Alonso singles on a line drive to left fielder Jurickson Profar.

2022-07-23	FF	94.4	2406	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Called Strike	
Pete Alonso singles on a line drive to left fielder Jurickson Profar.

2022-07-23	CU	72.2	2158	Crismatt, Nabil(R)	Alonso, Pete(R)	105.8	17°	339	
0-0	Bot 6	Hit Into Play	
Pete Alonso lines out sharply to center fielder Trent Grisham.

2022-07-23	SI	94.5	2163	Rogers, Taylor(L)	Alonso, Pete(R)	85.9	14°	209	
2-2	Bot 9	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Nomar Mazara.

2022-07-23	ST	81.4	2618	Rogers, Taylor(L)	Alonso, Pete(R)	99.2	25°	301	
2-1	Bot 9	Foul	
Pete Alonso singles on a line drive to right fielder Nomar Mazara.

2022-07-23	SI	94.5	2209	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
2-0	Bot 9	Called Strike	
Pete Alonso singles on a line drive to right fielder Nomar Mazara.

2022-07-23	ST	78.9	2646	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Ball	
Pete Alonso singles on a line drive to right fielder Nomar Mazara.

2022-07-23	ST	81.3	2683	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Ball	
Pete Alonso singles on a line drive to right fielder Nomar Mazara.

2022-07-22	ST	80.3	2688	Darvish, Yu(R)	Alonso, Pete(R)	99.3	42°	313	
2-1	Bot 7	Hit Into Play	
Pete Alonso flies out to center fielder Trent Grisham.

2022-07-22	CU	71.5	2711	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-1	Bot 7	Ball	
Pete Alonso flies out to center fielder Trent Grisham.

2022-07-22	CU	71.4	2626	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Ball	
Pete Alonso flies out to center fielder Trent Grisham.

2022-07-22	CU	71.0	2745	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso flies out to center fielder Trent Grisham.

2022-07-22	ST	85.3	2795	Darvish, Yu(R)	Alonso, Pete(R)	103.2	-14°	11	
3-2	Bot 4	Hit Into Play	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	ST	82.7	2781	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
3-1	Bot 4	Swinging Strike	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	FC	90.1	2622	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
2-1	Bot 4	Ball	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	FC	90.7	2576	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-1	Bot 4	Ball	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	ST	83.8	2834	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Swinging Strike	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	ST	84.8	2896	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso singles on a ground ball to center fielder Trent Grisham.

2022-07-22	SL	87.6	2848	Darvish, Yu(R)	Alonso, Pete(R)	83.0	39°	272	
2-2	Bot 1	Hit Into Play	
Pete Alonso flies out to right fielder Nomar Mazara.

2022-07-22	ST	85.7	2729	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso flies out to right fielder Nomar Mazara.

2022-07-22	ST	85.5	2764	Darvish, Yu(R)	Alonso, Pete(R)	68.0	61°	161	
1-1	Bot 1	Foul	
Pete Alonso flies out to right fielder Nomar Mazara.

2022-07-22	ST	86.6	2791	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso flies out to right fielder Nomar Mazara.

2022-07-22	FC	92.2	2608	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso flies out to right fielder Nomar Mazara.

2022-07-22	ST	80.6	2728	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
0-2	Bot 9	Hit By Pitch	
Pete Alonso hit by pitch.

2022-07-22	ST	81.7	2751	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
0-1	Bot 9	Swinging Strike	
Pete Alonso hit by pitch.

2022-07-22	SI	94.5	2260	Rogers, Taylor(L)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Called Strike	
Pete Alonso hit by pitch.

2022-07-17	SL	83.6	2682	Sampson, Adrian(R)	Alonso, Pete(R)	75.4	59°	161	
3-2	Top 5	Hit Into Play	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	FF	93.2	1989	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
2-2	Top 5	Ball	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	FF	93.6	1948	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Ball	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	FF	91.9	1873	Sampson, Adrian(R)	Alonso, Pete(R)	105.2	-5°	22	
1-1	Top 5	Foul	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	SL	81.5	2600	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	SI	91.7	1956	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso singles on a pop up to first baseman Frank Schwindel. Brandon Nimmo scores. Starling Marte to 3rd.

2022-07-17	SL	84.2	2490	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-17	CH	84.5	1471	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-07-17	SI	90.8	1920	Sampson, Adrian(R)	Alonso, Pete(R)	78.9	-23°	5	
0-1	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-07-17	SI	91.5	1957	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso strikes out swinging.

2022-07-17	FF	93.4	2140	Sampson, Adrian(R)	Alonso, Pete(R)	91.4	53°	212	
2-2	Top 1	Hit Into Play	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	FF	92.9	1896	Sampson, Adrian(R)	Alonso, Pete(R)	108.7	20°	357	
2-2	Top 1	Foul	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	SI	92.2	1921	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	FF	93.2	2105	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	FF	91.6	2131	Sampson, Adrian(R)	Alonso, Pete(R)	110.9	24°	333	
0-1	Top 1	Foul	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	FF	92.1	2030	Sampson, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Swinging Strike	
Pete Alonso flies out to center fielder Christopher Morel.

2022-07-17	FF	95.6	2286	Wick, Rowan(R)	Alonso, Pete(R)	74.8	-55°	1	
0-0	Top 8	Hit Into Play	
Pete Alonso grounds out to first baseman Frank Schwindel. Francisco Lindor to 2nd.

2022-07-16	SV	84.8	2590	Stroman, Marcus(R)	Alonso, Pete(R)	108.6	16°	300	
1-0	Top 4	Hit Into Play	
Pete Alonso doubles (15) on a sharp line drive to center fielder Rafael Ortega. Francisco Lindor scores.

2022-07-16	SI	91.6	2277	Stroman, Marcus(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso doubles (15) on a sharp line drive to center fielder Rafael Ortega. Francisco Lindor scores.

2022-07-16	SI	92.3	2186	Smyly, Drew(L)	Alonso, Pete(R)	91.3	23°	316	
1-0	Top 3	Hit Into Play	
Pete Alonso lines out to left fielder Ian Happ.

2022-07-16	FC	90.0	2229	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso lines out to left fielder Ian Happ.

2022-07-16	FF	93.4	1885	Espinoza, Anderson(R)	Alonso, Pete(R)	87.7	-27°	4	
3-0	Top 7	Hit Into Play	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-16	FF	94.2	1905	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
2-0	Top 7	Ball	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-16	FF	92.3	1910	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
1-0	Top 7	Ball	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-16	FF	95.8	1896	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-16	SL	84.6	2385	Hughes, Brandon(L)	Alonso, Pete(R)	--	°		
1-2	Top 6	Swinging Strike Blocked	
Pete Alonso strikes out swinging, catcher Willson Contreras to first baseman Frank Schwindel.

2022-07-16	FF	93.5	2434	Hughes, Brandon(L)	Alonso, Pete(R)	56.5	54°	140	
1-2	Top 6	Foul	
Pete Alonso strikes out swinging, catcher Willson Contreras to first baseman Frank Schwindel.

2022-07-16	FF	94.0	2478	Hughes, Brandon(L)	Alonso, Pete(R)	--	°		
0-2	Top 6	Ball	
Pete Alonso strikes out swinging, catcher Willson Contreras to first baseman Frank Schwindel.

2022-07-16	FF	92.9	2386	Hughes, Brandon(L)	Alonso, Pete(R)	72.9	-2°	35	
0-1	Top 6	Foul	
Pete Alonso strikes out swinging, catcher Willson Contreras to first baseman Frank Schwindel.

2022-07-16	SL	82.0	2341	Hughes, Brandon(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Swinging Strike	
Pete Alonso strikes out swinging, catcher Willson Contreras to first baseman Frank Schwindel.

2022-07-16	KC	80.9	2179	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-2	Top 2	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-07-16	SI	93.8	2221	Smyly, Drew(L)	Alonso, Pete(R)	71.4	59°	187	
0-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-07-16	SI	91.7	2171	Stroman, Marcus(R)	Alonso, Pete(R)	111.2	-2°	26	
0-1	Top 1	Hit Into Play	
Pete Alonso reaches on a fielding error by third baseman P. J. Higgins. Brandon Nimmo to 3rd.

2022-07-16	SI	93.3	2204	Smyly, Drew(L)	Alonso, Pete(R)	73.4	33°	238	
0-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-07-16	SI	93.2	2251	Smyly, Drew(L)	Alonso, Pete(R)	--	°		
0-1	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-16	SI	92.5	2192	Stroman, Marcus(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso reaches on a fielding error by third baseman P. J. Higgins. Brandon Nimmo to 3rd.

2022-07-16	SI	93.1	2094	Smyly, Drew(L)	Alonso, Pete(R)	68.8	41°	223	
0-0	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-07-16	FF	95.4	2427	Givens, Mychal(R)	Alonso, Pete(R)	--	°		
0-2	Top 10	Hit By Pitch	
Pete Alonso hit by pitch. Brandon Nimmo scores. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-07-16	SL	87.4	2524	Givens, Mychal(R)	Alonso, Pete(R)	71.5	65°	165	
0-1	Top 10	Foul	
Pete Alonso hit by pitch. Brandon Nimmo scores. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-07-16	FF	93.7	2299	Givens, Mychal(R)	Alonso, Pete(R)	72.8	42°	213	
0-0	Top 10	Foul	
Pete Alonso hit by pitch. Brandon Nimmo scores. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-07-16	FF	94.2	2491	Givens, Mychal(R)	Alonso, Pete(R)	79.6	31°	281	
2-1	Top 11	Hit Into Play	
Pete Alonso out on a sacrifice fly to right fielder Seiya Suzuki. Luis Guillorme scores. Throwing error by right fielder Seiya Suzuki.

2022-07-16	FF	94.5	2477	Givens, Mychal(R)	Alonso, Pete(R)	80.3	72°	129	
2-0	Top 11	Foul	
Pete Alonso out on a sacrifice fly to right fielder Seiya Suzuki. Luis Guillorme scores. Throwing error by right fielder Seiya Suzuki.

2022-07-16	SI	90.3	2159	Effross, Scott(R)	Alonso, Pete(R)	79.9	-9°	12	
2-1	Top 8	Hit Into Play	
Pete Alonso grounds out, third baseman P. J. Higgins to first baseman Frank Schwindel.

2022-07-16	FF	93.4	1903	Espinoza, Anderson(R)	Alonso, Pete(R)	104.5	-16°	8	
2-1	Top 5	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Nico Hoerner to second baseman David Bote to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-16	FF	94.2	2408	Givens, Mychal(R)	Alonso, Pete(R)	--	°		
1-0	Top 11	Ball	
Pete Alonso out on a sacrifice fly to right fielder Seiya Suzuki. Luis Guillorme scores. Throwing error by right fielder Seiya Suzuki.

2022-07-16	SI	91.3	2193	Effross, Scott(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso grounds out, third baseman P. J. Higgins to first baseman Frank Schwindel.

2022-07-16	SL	81.1	2049	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
1-1	Top 5	Blocked Ball	
Pete Alonso grounds into a double play, shortstop Nico Hoerner to second baseman David Bote to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-16	FF	93.5	2446	Givens, Mychal(R)	Alonso, Pete(R)	--	°		
0-0	Top 11	Ball	
Pete Alonso out on a sacrifice fly to right fielder Seiya Suzuki. Luis Guillorme scores. Throwing error by right fielder Seiya Suzuki.

2022-07-16	CH	82.9	2051	Effross, Scott(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Ball	
Pete Alonso grounds out, third baseman P. J. Higgins to first baseman Frank Schwindel.

2022-07-16	SL	79.1	2049	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso grounds into a double play, shortstop Nico Hoerner to second baseman David Bote to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-16	SL	80.3	2432	Effross, Scott(R)	Alonso, Pete(R)	48.4	8°	55	
0-0	Top 8	Foul	
Pete Alonso grounds out, third baseman P. J. Higgins to first baseman Frank Schwindel.

2022-07-16	FF	93.7	1867	Espinoza, Anderson(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso grounds into a double play, shortstop Nico Hoerner to second baseman David Bote to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-14	FF	94.0	2184	Thompson, Keegan(R)	Alonso, Pete(R)	--	°		
3-0	Top 5	Hit By Pitch	
Pete Alonso hit by pitch.

2022-07-14	ST	83.9	2966	Thompson, Keegan(R)	Alonso, Pete(R)	--	°		
2-0	Top 5	Ball	
Pete Alonso hit by pitch.

2022-07-14	SI	93.3	2425	Thompson, Keegan(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Ball	
Pete Alonso hit by pitch.

2022-07-14	FF	94.1	2444	Thompson, Keegan(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso hit by pitch.

2022-07-14	SI	90.8	1887	Leiter Jr., Mark(R)	Alonso, Pete(R)	108.6	24°	423	
0-1	Top 8	Hit Into Play	
Pete Alonso homers (24) on a fly ball to center field. Brandon Nimmo scores.

2022-07-14	FF	90.8	2006	Leiter Jr., Mark(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso homers (24) on a fly ball to center field. Brandon Nimmo scores.

2022-07-14	ST	83.4	2922	Thompson, Keegan(R)	Alonso, Pete(R)	89.6	2°	47	
0-1	Top 2	Hit Into Play	
Pete Alonso grounds into a double play, third baseman Patrick Wisdom to second baseman Christopher Morel to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-14	FF	94.2	2542	Thompson, Keegan(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso grounds into a double play, third baseman Patrick Wisdom to second baseman Christopher Morel to first baseman Alfonso Rivas. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-14	SI	90.8	1899	Leiter Jr., Mark(R)	Alonso, Pete(R)	61.0	9°	79	
1-0	Top 6	Hit Into Play	
Pete Alonso grounds out, shortstop Nico Hoerner to first baseman Alfonso Rivas.

2022-07-14	FF	90.9	1919	Leiter Jr., Mark(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out, shortstop Nico Hoerner to first baseman Alfonso Rivas.

2022-07-14	SI	93.5	2442	Thompson, Keegan(R)	Alonso, Pete(R)	84.4	-34°	3	
0-1	Top 1	Hit Into Play	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-14	FF	93.5	2331	Thompson, Keegan(R)	Alonso, Pete(R)	78.5	47°	236	
0-0	Top 1	Foul	
Pete Alonso grounds out, third baseman Patrick Wisdom to first baseman Alfonso Rivas.

2022-07-13	FF	93.8	2393	Morton, Charlie(R)	Alonso, Pete(R)	101.0	51°	292	
1-0	Top 5	Hit Into Play	
Pete Alonso flies out sharply to left fielder Adam Duvall.

2022-07-13	FF	93.9	2378	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso flies out sharply to left fielder Adam Duvall.

2022-07-13	CU	81.1	2975	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-2	Top 3	Called Strike	
Pete Alonso called out on strikes.

2022-07-13	FC	91.2	2637	Morton, Charlie(R)	Alonso, Pete(R)	68.4	-18°	7	
0-1	Top 3	Foul	
Pete Alonso called out on strikes.

2022-07-13	CH	86.6	2113	Morton, Charlie(R)	Alonso, Pete(R)	109.8	8°	168	
0-0	Top 3	Foul	
Pete Alonso called out on strikes.

2022-07-13	FC	89.8	2305	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
1-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-13	SI	91.4	1980	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-2	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-07-13	CH	85.0	1649	Chavez, Jesse(R)	Alonso, Pete(R)	85.2	9°	115	
0-1	Top 7	Foul	
Pete Alonso strikes out swinging.

2022-07-13	FC	89.7	2206	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-13	SI	94.0	1847	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Called Strike	
Pete Alonso called out on strikes.

2022-07-13	SL	85.5	2704	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Swinging Strike	
Pete Alonso called out on strikes.

2022-07-13	SI	95.7	2075	Morton, Charlie(R)	Alonso, Pete(R)	115.8	12°	272	
3-1	Top 1	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Adam Duvall.

2022-07-13	SL	86.3	2592	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso called out on strikes.

2022-07-13	CU	76.7	3084	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso called out on strikes.

2022-07-13	FC	89.6	2533	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Adam Duvall.

2022-07-13	SI	95.6	2149	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Adam Duvall.

2022-07-13	FC	89.2	2627	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Ball	
Pete Alonso singles on a sharp line drive to left fielder Adam Duvall.

2022-07-13	FF	94.3	2315	Morton, Charlie(R)	Alonso, Pete(R)	73.9	22°	204	
0-0	Top 1	Foul	
Pete Alonso singles on a sharp line drive to left fielder Adam Duvall.

2022-07-12	FF	97.5	2305	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-0	Top 5	Ball	
Spencer Strider intentionally walks Pete Alonso.

2022-07-12	FF	96.5	2286	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Ball	
Spencer Strider intentionally walks Pete Alonso.

2022-07-12	FF	96.5	2362	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Spencer Strider intentionally walks Pete Alonso.

2022-07-12	SL	87.3	2394	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-12	FF	99.1	2330	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-07-12	SL	86.2	2326	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-07-12	FF	98.3	2371	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-07-12	FF	97.5	2374	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-12	FF	97.4	2361	Strider, Spencer(R)	Alonso, Pete(R)	81.1	56°	222	
2-1	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-07-12	FF	98.3	2361	Strider, Spencer(R)	Alonso, Pete(R)	78.5	14°	160	
2-0	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-07-12	FF	97.9	2342	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-07-12	ST	82.0	2814	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-2	Top 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-12	ST	82.2	2690	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-12	FF	97.1	2336	Strider, Spencer(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-07-12	FC	90.4	2449	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso strikes out swinging.

2022-07-12	FC	90.2	2499	McHugh, Collin(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso strikes out swinging.

2022-07-11	CH	89.0	1176	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-11	CU	75.4	2642	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-1	Top 4	Called Strike	
Pete Alonso strikes out swinging.

2022-07-11	FF	93.4	1989	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-07-11	FF	93.7	2053	Fried, Max(L)	Alonso, Pete(R)	75.5	26°	220	
0-0	Top 4	Foul	
Pete Alonso strikes out swinging.

2022-07-11	CU	76.4	2693	Fried, Max(L)	Alonso, Pete(R)	93.2	-1°	42	
0-0	Top 3	Hit Into Play	
Pete Alonso doubles (14) on a sharp ground ball to left fielder Eddie Rosario, deflected by third baseman Austin Riley. Brandon Nimmo scores.

2022-07-11	CU	76.9	3110	Stephens, Jackson(R)	Alonso, Pete(R)	82.6	-11°	10	
2-2	Top 9	Hit Into Play	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	CH	86.2	1434	Lee, Dylan(L)	Alonso, Pete(R)	98.3	-2°	24	
0-2	Top 7	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Dansby Swanson to second baseman Robinson Cano to first baseman Matt Olson. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-11	FF	93.8	2343	Lee, Dylan(L)	Alonso, Pete(R)	67.3	41°	193	
0-2	Top 7	Foul	
Pete Alonso grounds into a double play, shortstop Dansby Swanson to second baseman Robinson Cano to first baseman Matt Olson. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-11	CU	77.3	3076	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Foul	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	SI	95.4	1990	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Foul	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	FF	92.1	2240	Lee, Dylan(L)	Alonso, Pete(R)	61.5	66°	130	
0-1	Top 7	Foul	
Pete Alonso grounds into a double play, shortstop Dansby Swanson to second baseman Robinson Cano to first baseman Matt Olson. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-11	FF	92.4	2228	Lee, Dylan(L)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso grounds into a double play, shortstop Dansby Swanson to second baseman Robinson Cano to first baseman Matt Olson. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-11	FF	96.0	2059	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-2	Top 1	Called Strike	
Pete Alonso called out on strikes.

2022-07-11	SI	94.0	1884	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Foul Tip	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	SI	94.3	1930	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Ball	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	FF	95.6	2240	Fried, Max(L)	Alonso, Pete(R)	68.5	52°	196	
0-2	Top 1	Foul	
Pete Alonso called out on strikes.

2022-07-11	FF	95.8	2144	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Top 1	Called Strike	
Pete Alonso called out on strikes.

2022-07-11	CU	78.8	2955	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-11	CU	74.3	2701	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso called out on strikes.

2022-07-11	CU	77.0	2978	Stephens, Jackson(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso grounds into a force out, third baseman Austin Riley to second baseman Robinson Cano. Brandon Nimmo scores. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-10	FF	99.7	2115	Alcantara, Sandy(R)	Alonso, Pete(R)	79.7	64°	140	
1-2	Bot 6	Hit Into Play	
Pete Alonso pops out to first baseman Garrett Cooper.

2022-07-10	FF	100.3	2146	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-2	Bot 6	Ball	
Pete Alonso pops out to first baseman Garrett Cooper.

2022-07-10	FF	98.5	2259	Alcantara, Sandy(R)	Alonso, Pete(R)	81.5	73°	135	
0-1	Bot 6	Foul	
Pete Alonso pops out to first baseman Garrett Cooper.

2022-07-10	FF	98.7	2239	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Swinging Strike	
Pete Alonso pops out to first baseman Garrett Cooper.

2022-07-10	SI	96.2	2299	Alcantara, Sandy(R)	Alonso, Pete(R)	103.5	10°	230	
0-0	Bot 4	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Jon Berti. Mark Canha to 2nd.

2022-07-10	SI	97.6	2197	Alcantara, Sandy(R)	Alonso, Pete(R)	79.5	28°	279	
0-1	Bot 2	Hit Into Play	
Pete Alonso lines out to left fielder Jon Berti.

2022-07-10	SI	95.5	2339	Alcantara, Sandy(R)	Alonso, Pete(R)	86.6	45°	248	
0-0	Bot 2	Foul	
Pete Alonso lines out to left fielder Jon Berti.

2022-07-10	SL	86.5	2194	Bass, Anthony(R)	Alonso, Pete(R)	102.7	45°	309	
0-0	Bot 8	Hit Into Play	
Pete Alonso flies out sharply to left fielder Luke Williams.

2022-07-09	SL	84.1	2303	Garrett, Braxton(L)	Alonso, Pete(R)	112.3	27°	418	
0-1	Bot 4	Hit Into Play	
Pete Alonso homers (23) on a fly ball to left field.

2022-07-09	FF	91.4	2246	Garrett, Braxton(L)	Alonso, Pete(R)	74.0	56°	189	
0-0	Bot 4	Foul	
Pete Alonso homers (23) on a fly ball to left field.

2022-07-09	SL	83.7	2270	Garrett, Braxton(L)	Alonso, Pete(R)	83.3	38°	283	
1-2	Bot 2	Hit Into Play	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-07-09	FF	91.7	2375	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
1-1	Bot 2	Called Strike	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-07-09	FF	91.7	2422	Garrett, Braxton(L)	Alonso, Pete(R)	74.4	45°	211	
1-0	Bot 2	Foul	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-07-09	CU	77.8	2262	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-07-09	SL	84.6	1909	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-09	SI	92.8	2079	Floro, Dylan(R)	Alonso, Pete(R)	37.4	-8°	13	
2-2	Bot 6	Foul	
Pete Alonso strikes out swinging.

2022-07-09	SL	87.3	2205	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
2-2	Bot 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-09	SL	84.8	1893	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso strikes out swinging.

2022-07-09	SL	86.1	2153	Bass, Anthony(R)	Alonso, Pete(R)	78.0	62°	175	
2-1	Bot 9	Foul	
Pete Alonso strikes out swinging.

2022-07-09	FF	91.8	2233	Floro, Dylan(R)	Alonso, Pete(R)	73.3	25°	210	
1-1	Bot 6	Foul	
Pete Alonso strikes out swinging.

2022-07-09	SI	94.6	1957	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
2-0	Bot 9	Foul Tip	
Pete Alonso strikes out swinging.

2022-07-09	CH	84.3	1706	Floro, Dylan(R)	Alonso, Pete(R)	65.2	82°	70	
1-0	Bot 6	Foul	
Pete Alonso strikes out swinging.

2022-07-09	SI	94.1	2016	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-07-09	SI	94.6	1925	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-07-09	SI	91.8	2200	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso strikes out swinging.

2022-07-08	CH	88.8	2070	López, Pablo(R)	Alonso, Pete(R)	102.7	-40°	3	
1-1	Bot 3	Hit Into Play	
Pete Alonso grounds out sharply, third baseman Joey Wendle to first baseman Garrett Cooper.

2022-07-08	FF	93.3	2181	López, Pablo(R)	Alonso, Pete(R)	--	°	12	
1-0	Bot 3	Swinging Strike	
Pete Alonso grounds out sharply, third baseman Joey Wendle to first baseman Garrett Cooper.

2022-07-08	CU	80.8	2448	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Blocked Ball	
Pete Alonso grounds out sharply, third baseman Joey Wendle to first baseman Garrett Cooper.

2022-07-08	SI	93.5	2005	López, Pablo(R)	Alonso, Pete(R)	105.8	6°	173	
1-2	Bot 2	Hit Into Play	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	CH	87.9	1994	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-2	Bot 2	Foul	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	CU	80.1	2501	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-2	Bot 2	Ball	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	FF	94.6	2201	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-2	Bot 2	Foul	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	CH	87.5	1906	López, Pablo(R)	Alonso, Pete(R)	68.1	-32°	2	
0-2	Bot 2	Foul	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	CH	87.1	1827	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Swinging Strike	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	SI	92.0	1923	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Called Strike	
Pete Alonso lines out sharply to second baseman Jon Berti.

2022-07-08	SL	82.7	2561	Okert, Steven(L)	Alonso, Pete(R)	--	°		
0-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-08	SL	82.3	2539	Okert, Steven(L)	Alonso, Pete(R)	86.6	-13°	6	
0-1	Bot 8	Foul	
Pete Alonso strikes out swinging.

2022-07-08	SL	79.5	2471	Okert, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-08	SI	92.2	2212	Floro, Dylan(R)	Alonso, Pete(R)	44.8	43°	108	
1-1	Bot 6	Hit Into Play	
Pete Alonso pops out softly to first baseman Garrett Cooper.

2022-07-08	SL	85.4	1921	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso pops out softly to first baseman Garrett Cooper.

2022-07-08	SI	92.0	2175	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso pops out softly to first baseman Garrett Cooper.

2022-07-07	FC	88.9	2434	Castano, Daniel(L)	Alonso, Pete(R)	113.5	-2°	40	
0-2	Bot 3	Hit Into Play	
Pete Alonso grounds out, third baseman Brian Anderson to first baseman Jesus Aguilar.

2022-07-07	SL	83.2	2529	Castano, Daniel(L)	Alonso, Pete(R)	64.8	-27°	3	
0-2	Bot 3	Foul	
Pete Alonso grounds out, third baseman Brian Anderson to first baseman Jesus Aguilar.

2022-07-07	FF	92.2	2266	Castano, Daniel(L)	Alonso, Pete(R)	71.6	59°	175	
0-1	Bot 3	Foul	
Pete Alonso grounds out, third baseman Brian Anderson to first baseman Jesus Aguilar.

2022-07-07	FC	86.5	2349	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso grounds out, third baseman Brian Anderson to first baseman Jesus Aguilar.

2022-07-07	FC	88.1	2470	Castano, Daniel(L)	Alonso, Pete(R)	86.3	47°	248	
0-0	Bot 1	Hit Into Play	
Pete Alonso flies out to center fielder Jesus Sanchez.

2022-07-07	SI	96.6	2169	Pop, Zach(R)	Alonso, Pete(R)	110.0	-10°	8	
0-1	Bot 6	Hit Into Play	
Pete Alonso grounds out, shortstop Jon Berti to first baseman Jesus Aguilar.

2022-07-07	SI	93.5	2190	Yacabonis, Jimmy(R)	Alonso, Pete(R)	84.0	-31°	3	
0-0	Bot 5	Hit Into Play	
Pete Alonso grounds out, third baseman Brian Anderson to first baseman Jesus Aguilar.

2022-07-07	SI	97.2	2097	Pop, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso grounds out, shortstop Jon Berti to first baseman Jesus Aguilar.

2022-07-06	SI	96.9	2266	Ashcraft, Graham(R)	Alonso, Pete(R)	107.4	18°	389	
0-1	Top 5	Hit Into Play	
Pete Alonso doubles (13) on a sharp line drive to left fielder Tommy Pham.

2022-07-06	FC	97.5	2332	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso doubles (13) on a sharp line drive to left fielder Tommy Pham.

2022-07-06	SI	95.7	2118	Ashcraft, Graham(R)	Alonso, Pete(R)	112.8	-1°	39	
3-2	Top 3	Hit Into Play	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	SI	95.1	2125	Ashcraft, Graham(R)	Alonso, Pete(R)	83.7	-37°	2	
3-1	Top 3	Foul	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	FC	97.2	2312	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
3-0	Top 3	Called Strike	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	FC	96.1	2323	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
2-0	Top 3	Ball	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	SI	94.3	1967	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
1-0	Top 3	Blocked Ball	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	FC	96.6	2239	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso singles on a sharp ground ball to left fielder Tommy Pham. Starling Marte to 2nd.

2022-07-06	SL	87.6	2676	Ashcraft, Graham(R)	Alonso, Pete(R)	107.3	1°	61	
2-2	Top 1	Hit Into Play	
Pete Alonso singles on a sharp ground ball to right fielder Albert Almora Jr. , deflected by second baseman Matt Reynolds. Brandon Nimmo to 3rd.

2022-07-06	FF	96.1	2224	Strickland, Hunter(R)	Alonso, Pete(R)	87.9	84°	27	
0-0	Top 9	Hit Into Play	
Pete Alonso pops out to catcher Michael Papierski in foul territory.

2022-07-06	FC	99.4	2208	Ashcraft, Graham(R)	Alonso, Pete(R)	76.2	67°	125	
2-1	Top 1	Foul	
Pete Alonso singles on a sharp ground ball to right fielder Albert Almora Jr. , deflected by second baseman Matt Reynolds. Brandon Nimmo to 3rd.

2022-07-06	FC	97.4	2455	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
2-0	Top 1	Foul	
Pete Alonso singles on a sharp ground ball to right fielder Albert Almora Jr. , deflected by second baseman Matt Reynolds. Brandon Nimmo to 3rd.

2022-07-06	SI	97.9	2177	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Blocked Ball	
Pete Alonso singles on a sharp ground ball to right fielder Albert Almora Jr. , deflected by second baseman Matt Reynolds. Brandon Nimmo to 3rd.

2022-07-06	FC	98.4	2336	Ashcraft, Graham(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso singles on a sharp ground ball to right fielder Albert Almora Jr. , deflected by second baseman Matt Reynolds. Brandon Nimmo to 3rd.

2022-07-06	SL	86.7	2203	Kuhnel, Joel(R)	Alonso, Pete(R)	81.6	9°	135	
0-2	Top 7	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Tommy Pham.

2022-07-06	SL	84.8	2283	Kuhnel, Joel(R)	Alonso, Pete(R)	69.0	26°	192	
0-1	Top 7	Foul	
Pete Alonso singles on a ground ball to left fielder Tommy Pham.

2022-07-06	SL	84.5	2322	Kuhnel, Joel(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso singles on a ground ball to left fielder Tommy Pham.

2022-07-05	CU	83.3	2826	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
2-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-05	SI	94.7	2356	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-2	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-07-05	SI	95.1	2509	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-1	Top 4	Called Strike	
Pete Alonso strikes out swinging.

2022-07-05	CU	82.8	2665	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-0	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-05	SI	94.4	2384	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-07-05	CU	83.2	2656	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
2-2	Top 1	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-07-05	CU	83.0	2563	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso strikes out on a foul tip.

2022-07-05	CU	83.5	2723	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-1	Top 1	Swinging Strike	
Pete Alonso strikes out on a foul tip.

2022-07-05	SI	94.3	2229	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
1-0	Top 1	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-07-05	CH	88.3	1785	Lodolo, Nick(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out on a foul tip.

2022-07-05	FF	95.3	2371	Hoffman, Jeff(R)	Alonso, Pete(R)	98.4	-5°	28	
1-2	Top 8	Hit Into Play	
Pete Alonso grounds out, shortstop Matt Reynolds to first baseman Mike Moustakas.

2022-07-05	SL	82.5	2552	Hoffman, Jeff(R)	Alonso, Pete(R)	--	°		
1-2	Top 8	Foul	
Pete Alonso grounds out, shortstop Matt Reynolds to first baseman Mike Moustakas.

2022-07-05	SL	83.4	2789	Hoffman, Jeff(R)	Alonso, Pete(R)	--	°		
0-2	Top 8	Ball	
Pete Alonso grounds out, shortstop Matt Reynolds to first baseman Mike Moustakas.

2022-07-05	FF	94.9	2497	Hoffman, Jeff(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Swinging Strike	
Pete Alonso grounds out, shortstop Matt Reynolds to first baseman Mike Moustakas.

2022-07-05	FF	94.4	2468	Hoffman, Jeff(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Swinging Strike	
Pete Alonso grounds out, shortstop Matt Reynolds to first baseman Mike Moustakas.

2022-07-05	SL	84.8	2222	Kuhnel, Joel(R)	Alonso, Pete(R)	75.0	-37°	2	
1-2	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Brandon Drury to first baseman Mike Moustakas.

2022-07-05	SL	84.4	2310	Kuhnel, Joel(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Called Strike	
Pete Alonso grounds out, third baseman Brandon Drury to first baseman Mike Moustakas.

2022-07-05	SI	93.3	2124	Kuhnel, Joel(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso grounds out, third baseman Brandon Drury to first baseman Mike Moustakas.

2022-07-05	SL	83.8	2323	Kuhnel, Joel(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso grounds out, third baseman Brandon Drury to first baseman Mike Moustakas.

2022-07-04	FF	99.6	2402	Greene, Hunter(R)	Alonso, Pete(R)	59.5	68°	92	
3-1	Top 5	Hit Into Play	
Pete Alonso pops out softly to first baseman Joey Votto.

2022-07-04	SL	89.5	2402	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
3-0	Top 5	Called Strike	
Pete Alonso pops out softly to first baseman Joey Votto.

2022-07-04	FF	99.8	2385	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
2-0	Top 5	Ball	
Pete Alonso pops out softly to first baseman Joey Votto.

2022-07-04	SL	89.1	2417	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Ball	
Pete Alonso pops out softly to first baseman Joey Votto.

2022-07-04	FF	99.2	2390	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso pops out softly to first baseman Joey Votto.

2022-07-04	SL	86.3	2157	Greene, Hunter(R)	Alonso, Pete(R)	101.6	13°	273	
0-0	Top 3	Hit Into Play	
Pete Alonso lines out sharply to right fielder Albert Almora Jr.

2022-07-04	FF	97.5	2394	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
3-2	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	SL	87.1	2375	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
3-1	Top 1	Swinging Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	FF	97.0	2390	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	SL	88.9	2343	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	SL	85.5	2288	Greene, Hunter(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	FF	95.3	2278	Greene, Hunter(R)	Alonso, Pete(R)	70.4	43°	189	
0-0	Top 1	Foul	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-07-04	SI	94.6	2175	Cessa, Luis(R)	Alonso, Pete(R)	108.1	-9°	15	
0-0	Top 7	Hit Into Play	
Pete Alonso grounds out sharply, pitcher Luis Cessa to first baseman Joey Votto. Francisco Lindor to 2nd.

2022-07-04	FF	96.8	2340	Moreta, Dauri(R)	Alonso, Pete(R)	116.5	17°	352	
1-0	Top 9	Hit Into Play	
Pete Alonso doubles (12) on a sharp line drive to left fielder Tommy Pham.

2022-07-04	FF	96.6	2343	Moreta, Dauri(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso doubles (12) on a sharp line drive to left fielder Tommy Pham.

2022-07-03	ST	87.4	2512	Gray, Jon(R)	Alonso, Pete(R)	68.8	54°	161	
1-2	Bot 5	Hit Into Play	
Pete Alonso pops out to second baseman Marcus Semien.

2022-07-03	FF	96.8	2045	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-2	Bot 5	Ball	
Pete Alonso pops out to second baseman Marcus Semien.

2022-07-03	FF	96.3	2054	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Foul Tip	
Pete Alonso pops out to second baseman Marcus Semien.

2022-07-03	ST	85.6	2540	Gray, Jon(R)	Alonso, Pete(R)	53.5	0°	31	
0-0	Bot 5	Foul	
Pete Alonso pops out to second baseman Marcus Semien.

2022-07-03	ST	86.7	2745	Gray, Jon(R)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Swinging Strike	
Pete Alonso strikes out swinging. Pete Alonso advances to 2nd, on a throwing error by catcher Jonah Heim.

2022-07-03	ST	85.3	2623	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Ball	
Pete Alonso strikes out swinging. Pete Alonso advances to 2nd, on a throwing error by catcher Jonah Heim.

2022-07-03	ST	84.9	2552	Gray, Jon(R)	Alonso, Pete(R)	65.7	48°	173	
0-2	Bot 4	Foul	
Pete Alonso strikes out swinging. Pete Alonso advances to 2nd, on a throwing error by catcher Jonah Heim.

2022-07-03	FF	95.9	1934	Gray, Jon(R)	Alonso, Pete(R)	77.8	17°	176	
0-1	Bot 4	Foul	
Pete Alonso strikes out swinging. Pete Alonso advances to 2nd, on a throwing error by catcher Jonah Heim.

2022-07-03	FF	96.0	1993	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso strikes out swinging. Pete Alonso advances to 2nd, on a throwing error by catcher Jonah Heim.

2022-07-03	FF	97.8	2098	Gray, Jon(R)	Alonso, Pete(R)	89.6	-8°	17	
2-2	Bot 1	Hit Into Play	
Pete Alonso grounds out, second baseman Marcus Semien to first baseman Nathaniel Lowe.

2022-07-03	SL	85.9	1293	Gray, Jon(R)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Swinging Strike	
Pete Alonso grounds out, second baseman Marcus Semien to first baseman Nathaniel Lowe.

2022-07-03	ST	85.8	2593	Gray, Jon(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso grounds out, second baseman Marcus Semien to first baseman Nathaniel Lowe.

2022-07-03	FF	96.1	2171	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso grounds out, second baseman Marcus Semien to first baseman Nathaniel Lowe.

2022-07-03	ST	85.0	2513	Gray, Jon(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Swinging Strike	
Pete Alonso grounds out, second baseman Marcus Semien to first baseman Nathaniel Lowe.

2022-07-03	SL	82.0	2541	Leclerc, José(R)	Alonso, Pete(R)	91.8	34°	326	
1-0	Bot 7	Hit Into Play	
Pete Alonso flies out to left fielder Kole Calhoun.

2022-07-03	SL	81.2	2550	Leclerc, José(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso flies out to left fielder Kole Calhoun.

2022-07-02	FC	90.6	2269	Pérez, Martín(L)	Alonso, Pete(R)	93.1	6°	119	
0-0	Bot 5	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Corey Seager to second baseman Marcus Semien to first baseman Nathaniel Lowe. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-07-02	FC	90.7	2268	Pérez, Martín(L)	Alonso, Pete(R)	102.2	0°	44	
3-1	Bot 3	Hit Into Play	
Pete Alonso grounds into a force out, pitcher Martin Perez to shortstop Corey Seager to second baseman Marcus Semien. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-02	SI	94.6	2075	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
2-1	Bot 3	Ball	
Pete Alonso grounds into a force out, pitcher Martin Perez to shortstop Corey Seager to second baseman Marcus Semien. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-02	FF	92.4	1932	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso grounds into a force out, pitcher Martin Perez to shortstop Corey Seager to second baseman Marcus Semien. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-02	CH	84.0	1627	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso grounds into a force out, pitcher Martin Perez to shortstop Corey Seager to second baseman Marcus Semien. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-02	FF	94.8	1978	Pérez, Martín(L)	Alonso, Pete(R)	65.7	39°	178	
0-0	Bot 3	Foul	
Pete Alonso grounds into a force out, pitcher Martin Perez to shortstop Corey Seager to second baseman Marcus Semien. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-07-02	FC	87.6	2172	Pérez, Martín(L)	Alonso, Pete(R)	73.8	50°	194	
1-2	Bot 1	Hit Into Play	
Pete Alonso pops out to shortstop Corey Seager.

2022-07-02	SI	94.8	1972	Pérez, Martín(L)	Alonso, Pete(R)	76.1	13°	132	
1-2	Bot 1	Foul	
Pete Alonso pops out to shortstop Corey Seager.

2022-07-02	FF	93.6	2017	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Called Strike	
Pete Alonso pops out to shortstop Corey Seager.

2022-07-02	FC	88.8	2184	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso pops out to shortstop Corey Seager.

2022-07-02	FF	94.3	2076	Pérez, Martín(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso pops out to shortstop Corey Seager.

2022-07-02	SL	88.1	2622	Santana, Dennis(R)	Alonso, Pete(R)	--	°		
1-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-07-02	SL	87.7	2642	Santana, Dennis(R)	Alonso, Pete(R)	--	°		
0-2	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-07-02	FF	97.5	2342	Santana, Dennis(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Foul	
Pete Alonso strikes out swinging.

2022-07-02	SL	86.8	2560	Santana, Dennis(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-07-01	SI	90.9	2214	Otto, Glenn(R)	Alonso, Pete(R)	75.7	49°	204	
0-0	Bot 4	Hit Into Play	
Pete Alonso pops out to second baseman Marcus Semien.

2022-07-01	ST	80.4	2415	Otto, Glenn(R)	Alonso, Pete(R)	104.1	-6°	16	
1-1	Bot 1	Hit Into Play	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia. Francisco Lindor to 2nd.

2022-07-01	FF	91.1	2278	Otto, Glenn(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia. Francisco Lindor to 2nd.

2022-07-01	FF	95.6	2262	Burke, Brock(L)	Alonso, Pete(R)	109.7	2°	82	
1-1	Bot 6	Hit Into Play	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia.

2022-07-01	CU	84.9	2323	Martin, Brett(L)	Alonso, Pete(R)	--	°		
3-2	Bot 8	Blocked Ball	
Pete Alonso walks.

2022-07-01	SI	92.3	2206	Otto, Glenn(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia. Francisco Lindor to 2nd.

2022-07-01	FF	95.4	2282	Burke, Brock(L)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia.

2022-07-01	SI	95.5	2343	Martin, Brett(L)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Ball	
Pete Alonso walks.

2022-07-01	FF	94.6	2176	Burke, Brock(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Foul	
Pete Alonso singles on a sharp ground ball to right fielder Adolis Garcia.

2022-07-01	CU	84.2	2351	Martin, Brett(L)	Alonso, Pete(R)	--	°		
1-2	Bot 8	Ball	
Pete Alonso walks.

2022-07-01	CU	84.4	2306	Martin, Brett(L)	Alonso, Pete(R)	--	°		
0-2	Bot 8	Ball	
Pete Alonso walks.

2022-07-01	FF	93.9	2208	Martin, Brett(L)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Called Strike	
Pete Alonso walks.

2022-07-01	CU	84.5	2337	Martin, Brett(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Swinging Strike Blocked	
Pete Alonso walks.

2022-06-29	FF	94.5	2581	Verlander, Justin(R)	Alonso, Pete(R)	99.1	62°	198	
2-0	Bot 7	Hit Into Play	
Pete Alonso pops out to shortstop Jeremy Pena.

2022-06-29	FF	94.3	2458	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso pops out to shortstop Jeremy Pena.

2022-06-29	SL	86.2	2548	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso pops out to shortstop Jeremy Pena.

2022-06-29	SL	90.5	2578	Verlander, Justin(R)	Alonso, Pete(R)	52.5	-45°	1	
0-1	Bot 4	Hit Into Play	
Pete Alonso grounds out softly, third baseman Alex Bregman to first baseman Yuli Gurriel.

2022-06-29	SL	89.5	2486	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Swinging Strike	
Pete Alonso grounds out softly, third baseman Alex Bregman to first baseman Yuli Gurriel.

2022-06-29	FF	96.5	2470	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks.

2022-06-29	FF	96.1	2505	Verlander, Justin(R)	Alonso, Pete(R)	88.3	23°	267	
3-2	Bot 1	Foul	
Pete Alonso walks.

2022-06-29	FF	96.1	2491	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso walks.

2022-06-29	SL	86.2	2537	Verlander, Justin(R)	Alonso, Pete(R)	98.7	46°	317	
2-1	Bot 1	Foul	
Pete Alonso walks.

2022-06-29	SL	86.7	2508	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso walks.

2022-06-29	SL	87.6	2505	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Called Strike	
Pete Alonso walks.

2022-06-29	SL	87.2	2499	Verlander, Justin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks.

2022-06-28	CH	89.7	1637	Valdez, Framber(L)	Alonso, Pete(R)	77.1	-6°	11	
1-0	Bot 6	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Kyle Tucker.

2022-06-28	SI	94.8	2138	Valdez, Framber(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso singles on a ground ball to right fielder Kyle Tucker.

2022-06-28	SI	94.3	2124	Valdez, Framber(L)	Alonso, Pete(R)	94.2	-10°	12	
0-0	Bot 4	Hit Into Play	
Pete Alonso grounds out, second baseman Jose Altuve to first baseman Yuli Gurriel. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-06-28	CU	79.3	2956	Valdez, Framber(L)	Alonso, Pete(R)	69.2	-16°	5	
3-2	Bot 1	Hit Into Play	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	SI	95.6	2272	Valdez, Framber(L)	Alonso, Pete(R)	100.3	27°	329	
3-2	Bot 1	Foul	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	CU	78.9	2997	Valdez, Framber(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Blocked Ball	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	SI	95.5	2189	Valdez, Framber(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Blocked Ball	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	CU	79.7	2930	Valdez, Framber(L)	Alonso, Pete(R)	96.6	-10°	10	
1-2	Bot 1	Foul	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	SI	95.2	2244	Valdez, Framber(L)	Alonso, Pete(R)	81.7	41°	241	
1-1	Bot 1	Foul	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	SI	94.3	2250	Valdez, Framber(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Called Strike	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-28	SI	94.3	2135	Valdez, Framber(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso grounds out, shortstop Jeremy Pena to first baseman Yuli Gurriel.

2022-06-26	FC	85.7	2254	Castano, Daniel(L)	Alonso, Pete(R)	95.1	50°	255	
0-0	Top 5	Hit Into Play	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	FF	91.7	2302	Castano, Daniel(L)	Alonso, Pete(R)	51.4	39°	133	
0-1	Top 3	Hit Into Play	
Pete Alonso doubles (11) on a fly ball to first baseman Jesus Aguilar. Starling Marte scores.

2022-06-26	FC	85.4	2355	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Foul Tip	
Pete Alonso doubles (11) on a fly ball to first baseman Jesus Aguilar. Starling Marte scores.

2022-06-26	FC	84.4	2293	Castano, Daniel(L)	Alonso, Pete(R)	86.0	50°	233	
3-1	Top 1	Hit Into Play	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	FC	85.6	2285	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
3-0	Top 1	Called Strike	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	FC	85.3	2302	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
2-0	Top 1	Ball	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	FF	92.5	2177	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
1-0	Top 1	Ball	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	FC	87.7	2273	Castano, Daniel(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso flies out to left fielder Jon Berti.

2022-06-26	SL	83.4	2525	Okert, Steven(L)	Alonso, Pete(R)	--	°		
3-2	Top 8	Ball	
Pete Alonso walks.

2022-06-26	FF	93.7	2259	Okert, Steven(L)	Alonso, Pete(R)	--	°		
2-2	Top 8	Ball	
Pete Alonso walks.

2022-06-26	FF	94.3	2172	Okert, Steven(L)	Alonso, Pete(R)	--	°		
2-1	Top 8	Called Strike	
Pete Alonso walks.

2022-06-26	SL	82.0	2591	Okert, Steven(L)	Alonso, Pete(R)	--	°		
2-0	Top 8	Called Strike	
Pete Alonso walks.

2022-06-26	SL	82.3	2542	Okert, Steven(L)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso walks.

2022-06-26	SL	81.6	2531	Okert, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso walks.

2022-06-25	CH	85.4	1476	Rogers, Trevor(L)	Alonso, Pete(R)	89.7	56°	212	
0-1	Top 4	Hit Into Play	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-06-25	FF	94.3	2479	Rogers, Trevor(L)	Alonso, Pete(R)	85.5	38°	272	
0-0	Top 4	Foul	
Pete Alonso flies out to right fielder Bryan De La Cruz.

2022-06-25	FF	94.4	2407	Rogers, Trevor(L)	Alonso, Pete(R)	101.1	31°	346	
0-1	Top 2	Hit Into Play	
Pete Alonso homers (21) on a fly ball to right field.

2022-06-25	FF	94.0	2363	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso homers (21) on a fly ball to right field.

2022-06-25	SI	94.3	2159	Yacabonis, Jimmy(R)	Alonso, Pete(R)	110.4	19°	433	
3-2	Top 8	Hit Into Play	
Pete Alonso homers (22) on a line drive to center field.

2022-06-25	SI	93.8	2241	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
2-2	Top 8	Ball	
Pete Alonso homers (22) on a line drive to center field.

2022-06-25	SI	99.0	2071	Pop, Zach(R)	Alonso, Pete(R)	39.1	40°	91	
1-2	Top 5	Hit Into Play	
Pete Alonso pops out to first baseman Garrett Cooper on the infield fly rule.

2022-06-25	SI	93.5	2220	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
2-1	Top 8	Called Strike	
Pete Alonso homers (22) on a line drive to center field.

2022-06-25	SI	97.9	1966	Pop, Zach(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Foul	
Pete Alonso pops out to first baseman Garrett Cooper on the infield fly rule.

2022-06-25	ST	80.8	2819	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso homers (22) on a line drive to center field.

2022-06-25	SI	98.2	1986	Pop, Zach(R)	Alonso, Pete(R)	--	°		
1-1	Top 5	Foul	
Pete Alonso pops out to first baseman Garrett Cooper on the infield fly rule.

2022-06-25	ST	81.3	2697	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso homers (22) on a line drive to center field.

2022-06-25	SI	97.6	1927	Pop, Zach(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Swinging Strike	
Pete Alonso pops out to first baseman Garrett Cooper on the infield fly rule.

2022-06-25	SI	98.8	2067	Pop, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Blocked Ball	
Pete Alonso pops out to first baseman Garrett Cooper on the infield fly rule.

2022-06-25	SI	93.7	2060	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso homers (22) on a line drive to center field.

2022-06-24	SI	98.5	2324	Alcantara, Sandy(R)	Alonso, Pete(R)	105.4	-31°	3	
1-0	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Luke Williams to first baseman Jesus Aguilar.

2022-06-24	SI	97.8	2351	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out, third baseman Luke Williams to first baseman Jesus Aguilar.

2022-06-24	SI	100.2	2456	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-06-24	SL	90.8	2468	Alcantara, Sandy(R)	Alonso, Pete(R)	63.2	-36°	3	
1-1	Top 4	Foul	
Pete Alonso strikes out on a foul tip.

2022-06-24	SI	99.4	2437	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-06-24	SL	90.4	2417	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso strikes out on a foul tip.

2022-06-24	SI	98.0	2328	Alcantara, Sandy(R)	Alonso, Pete(R)	95.3	18°	309	
1-0	Top 1	Hit Into Play	
Pete Alonso lines out to left fielder Jorge Soler.

2022-06-24	SI	97.5	2281	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso lines out to left fielder Jorge Soler.

2022-06-24	ST	82.0	2873	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-24	ST	82.1	2822	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
0-2	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-24	SI	95.7	2149	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-06-24	SI	94.6	2136	Yacabonis, Jimmy(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-06-22	FC	87.1	2390	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
2-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	FC	85.9	2454	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
2-1	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	SL	79.6	2593	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-06-22	FF	93.8	2416	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	FC	85.9	2328	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-06-22	FC	85.7	2371	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	FC	85.7	2415	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	FF	93.5	2454	Garcia, Luis(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-22	CH	91.0	2091	Montero, Rafael(R)	Alonso, Pete(R)	--	°		
3-2	Top 8	Called Strike	
Pete Alonso called out on strikes.

2022-06-22	CH	91.4	1903	Montero, Rafael(R)	Alonso, Pete(R)	--	°		
2-2	Top 8	Ball	
Pete Alonso called out on strikes.

2022-06-22	SI	96.1	2142	Montero, Rafael(R)	Alonso, Pete(R)	81.3	-26°	6	
2-1	Top 8	Foul	
Pete Alonso called out on strikes.

2022-06-22	SL	89.3	2369	Montero, Rafael(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso called out on strikes.

2022-06-22	SI	95.6	2146	Montero, Rafael(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso called out on strikes.

2022-06-22	FF	100.1	2465	Stanek, Ryne(R)	Alonso, Pete(R)	88.2	40°	286	
0-1	Top 6	Hit Into Play	
Pete Alonso out on a sacrifice fly to right fielder Kyle Tucker. Starling Marte scores.

2022-06-22	FF	95.6	2283	Montero, Rafael(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso called out on strikes.

2022-06-22	FF	99.4	2509	Stanek, Ryne(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Swinging Strike	
Pete Alonso out on a sacrifice fly to right fielder Kyle Tucker. Starling Marte scores.

2022-06-21	FF	95.8	2223	Urquidy, José(R)	Alonso, Pete(R)	107.8	25°	413	
2-2	Top 6	Hit Into Play	
Pete Alonso homers (20) on a fly ball to left center field.

2022-06-21	FF	95.7	2220	Urquidy, José(R)	Alonso, Pete(R)	68.7	21°	162	
2-1	Top 6	Foul	
Pete Alonso homers (20) on a fly ball to left center field.

2022-06-21	FF	94.9	2204	Urquidy, José(R)	Alonso, Pete(R)	--	°		
2-0	Top 6	Called Strike	
Pete Alonso homers (20) on a fly ball to left center field.

2022-06-21	CH	86.2	1931	Urquidy, José(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso homers (20) on a fly ball to left center field.

2022-06-21	FF	96.1	2256	Urquidy, José(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso homers (20) on a fly ball to left center field.

2022-06-21	FF	94.9	2128	Urquidy, José(R)	Alonso, Pete(R)	96.7	13°	224	
1-0	Top 4	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Jose Siri.

2022-06-21	FF	95.7	2247	Urquidy, José(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso singles on a line drive to center fielder Jose Siri.

2022-06-21	FF	92.8	2148	Urquidy, José(R)	Alonso, Pete(R)	--	°		
3-0	Top 2	Ball	
Pete Alonso walks.

2022-06-21	FF	92.0	2014	Urquidy, José(R)	Alonso, Pete(R)	--	°		
2-0	Top 2	Ball	
Pete Alonso walks.

2022-06-21	ST	80.4	2639	Urquidy, José(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso walks.

2022-06-21	FF	93.7	2139	Urquidy, José(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso walks.

2022-06-21	SI	93.1	2239	Martinez, Seth(R)	Alonso, Pete(R)	53.3	-55°	2	
3-2	Top 8	Hit Into Play	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-21	CH	86.7	1842	Martinez, Seth(R)	Alonso, Pete(R)	--	°		
2-2	Top 8	Ball	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-21	ST	81.5	2599	Martinez, Seth(R)	Alonso, Pete(R)	--	°		
2-1	Top 8	Called Strike	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-21	SI	92.1	2283	Martinez, Seth(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-21	ST	81.1	2574	Martinez, Seth(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Ball	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-21	ST	82.4	2599	Martinez, Seth(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso singles on a soft ground ball to third baseman Alex Bregman.

2022-06-20	CH	84.7	1152	Rogers, Trevor(L)	Alonso, Pete(R)	98.9	22°	332	
2-0	Bot 5	Hit Into Play	
Pete Alonso out on a sacrifice fly to left fielder Luke Williams. Brandon Nimmo scores.

2022-06-20	SL	80.8	1947	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Pete Alonso out on a sacrifice fly to left fielder Luke Williams. Brandon Nimmo scores.

2022-06-20	CH	84.5	1268	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso out on a sacrifice fly to left fielder Luke Williams. Brandon Nimmo scores.

2022-06-20	FF	97.0	2553	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-06-20	FF	95.2	2418	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
0-2	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-06-20	SL	79.6	2008	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Swinging Strike	
Pete Alonso called out on strikes.

2022-06-20	SL	80.4	2017	Rogers, Trevor(L)	Alonso, Pete(R)	68.2	69°	134	
0-0	Bot 3	Foul	
Pete Alonso called out on strikes.

2022-06-20	FF	96.1	2487	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-20	SL	88.3	2248	Bass, Anthony(R)	Alonso, Pete(R)	97.6	-34°	2	
1-2	Bot 7	Hit Into Play	
Pete Alonso grounds into a double play, second baseman Jazz Chisholm Jr. to first baseman Garrett Cooper. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-20	SL	82.0	2022	Rogers, Trevor(L)	Alonso, Pete(R)	61.8	19°	111	
3-2	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-06-20	SI	94.7	2036	Bass, Anthony(R)	Alonso, Pete(R)	63.4	40°	182	
1-2	Bot 7	Foul	
Pete Alonso grounds into a double play, second baseman Jazz Chisholm Jr. to first baseman Garrett Cooper. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-20	SL	81.3	2018	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-06-20	FF	93.8	2001	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Ball	
Pete Alonso grounds into a double play, second baseman Jazz Chisholm Jr. to first baseman Garrett Cooper. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-20	FF	94.9	2345	Rogers, Trevor(L)	Alonso, Pete(R)	93.0	34°	319	
2-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-06-20	SI	94.7	1998	Bass, Anthony(R)	Alonso, Pete(R)	67.6	-48°	2	
0-1	Bot 7	Foul	
Pete Alonso grounds into a double play, second baseman Jazz Chisholm Jr. to first baseman Garrett Cooper. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-20	FF	95.5	2328	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-06-20	CH	87.3	1231	Rogers, Trevor(L)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-06-20	SL	86.7	2307	Bass, Anthony(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso grounds into a double play, second baseman Jazz Chisholm Jr. to first baseman Garrett Cooper. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-20	FF	95.8	2287	Rogers, Trevor(L)	Alonso, Pete(R)	71.7	47°	192	
0-0	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-06-19	SI	97.3	2422	Alcantara, Sandy(R)	Alonso, Pete(R)	50.7	-1°	25	
0-1	Bot 6	Hit Into Play	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	SI	96.6	2358	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	SI	96.9	2364	Alcantara, Sandy(R)	Alonso, Pete(R)	100.8	-20°	5	
3-0	Bot 4	Hit Into Play	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	CH	91.3	2195	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
2-0	Bot 4	Ball	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	CH	92.0	2122	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Ball	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	SL	88.8	2533	Alcantara, Sandy(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Lewin Diaz.

2022-06-19	SL	86.8	2407	Alcantara, Sandy(R)	Alonso, Pete(R)	104.4	14°	326	
0-0	Bot 2	Hit Into Play	
Pete Alonso doubles (10) on a line drive to left fielder Luke Williams.

2022-06-19	FF	95.2	2656	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
3-0	Bot 9	Ball	
Pete Alonso walks.

2022-06-19	SL	88.8	2735	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
2-0	Bot 9	Ball	
Pete Alonso walks.

2022-06-19	SL	89.0	2726	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Ball	
Pete Alonso walks.

2022-06-19	FF	95.3	2570	Scott, Tanner(L)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Ball	
Pete Alonso walks.

2022-06-18	SL	85.3	2292	Garrett, Braxton(L)	Alonso, Pete(R)	91.9	50°	256	
0-1	Bot 3	Hit Into Play	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-06-18	CU	77.6	2229	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso flies out to right fielder Avisail Garcia.

2022-06-18	SL	83.7	1915	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-18	SI	91.1	2004	Floro, Dylan(R)	Alonso, Pete(R)	55.4	67°	96	
2-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-06-18	SL	83.9	2095	Garrett, Braxton(L)	Alonso, Pete(R)	88.8	46°	254	
3-1	Bot 2	Hit Into Play	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	FF	89.6	2186	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
1-2	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-06-18	CH	84.2	1887	Floro, Dylan(R)	Alonso, Pete(R)	58.9	-40°	3	
1-1	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-06-18	FF	92.7	2315	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
2-1	Bot 2	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	SI	91.4	2172	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Called Strike	
Pete Alonso strikes out swinging.

2022-06-18	SL	85.1	2444	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
1-1	Bot 2	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	FF	92.1	2304	Garrett, Braxton(L)	Alonso, Pete(R)	74.0	29°	222	
1-0	Bot 2	Foul	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	CH	85.0	1876	Floro, Dylan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-06-18	SL	82.8	2609	Head, Louis(R)	Alonso, Pete(R)	88.7	26°	331	
2-2	Bot 8	Hit Into Play	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	SL	82.9	2120	Garrett, Braxton(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	FF	94.5	2221	Head, Louis(R)	Alonso, Pete(R)	74.9	69°	148	
2-1	Bot 8	Foul	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	FF	94.1	2291	Head, Louis(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	SL	81.9	2696	Head, Louis(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-18	FF	93.8	2278	Head, Louis(R)	Alonso, Pete(R)	76.1	23°	213	
0-0	Bot 8	Foul	
Pete Alonso flies out to center fielder Bryan De La Cruz.

2022-06-17	FC	89.4	2348	López, Pablo(R)	Alonso, Pete(R)	78.0	-12°	8	
1-0	Bot 5	Hit Into Play	
Pete Alonso singles on a ground ball to center fielder Bryan De La Cruz, deflected by right fielder Avisail Garcia. Pete Alonso out at 2nd on the throw, center fielder Bryan De La Cruz to shortstop Miguel Rojas.

2022-06-17	FF	90.4	2331	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a ground ball to center fielder Bryan De La Cruz, deflected by right fielder Avisail Garcia. Pete Alonso out at 2nd on the throw, center fielder Bryan De La Cruz to shortstop Miguel Rojas.

2022-06-17	FF	93.4	2332	López, Pablo(R)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Ball	
Pete Alonso walks.

2022-06-17	FF	94.0	2400	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Ball	
Pete Alonso walks.

2022-06-17	CH	86.7	1883	López, Pablo(R)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Foul	
Pete Alonso walks.

2022-06-17	FF	93.2	2273	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso walks.

2022-06-17	CH	87.5	1890	López, Pablo(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Swinging Strike	
Pete Alonso walks.

2022-06-17	CH	87.0	1923	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso walks.

2022-06-17	FC	89.6	2212	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso walks.

2022-06-17	SI	92.9	2192	Nance, Tommy(R)	Alonso, Pete(R)	96.7	24°	368	
0-0	Bot 6	Hit Into Play	
Pete Alonso hits a grand slam (19) to left center field. J.D. Davis scores. Starling Marte scores. Francisco Lindor scores.

2022-06-17	FF	92.4	2201	Head, Louis(R)	Alonso, Pete(R)	80.2	41°	268	
0-1	Bot 8	Hit Into Play	
Pete Alonso flies out to left fielder Jorge Soler.

2022-06-17	SL	82.0	2478	Head, Louis(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso flies out to left fielder Jorge Soler.

2022-06-17	SI	92.6	1922	López, Pablo(R)	Alonso, Pete(R)	82.1	8°	129	
1-0	Bot 1	Hit Into Play	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Garrett Cooper.

2022-06-17	CH	86.8	1974	López, Pablo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso grounds out, shortstop Miguel Rojas to first baseman Garrett Cooper.

2022-06-16	SL	82.7	2545	Ashby, Aaron(L)	Alonso, Pete(R)	83.0	21°	274	
1-2	Bot 4	Hit Into Play	
Pete Alonso lines out to left fielder Christian Yelich.

2022-06-16	CU	81.2	2435	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Ball	
Pete Alonso lines out to left fielder Christian Yelich.

2022-06-16	CU	80.8	2681	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Swinging Strike	
Pete Alonso lines out to left fielder Christian Yelich.

2022-06-16	SI	96.0	2234	Ashby, Aaron(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso lines out to left fielder Christian Yelich.

2022-06-16	FF	92.6	2410	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
3-2	Bot 7	Ball	
Pete Alonso walks.

2022-06-16	FF	93.8	2456	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
3-1	Bot 7	Called Strike	
Pete Alonso walks.

2022-06-16	CH	82.1	1264	Boxberger, Brad(R)	Alonso, Pete(R)	99.8	16°	199	
3-0	Bot 7	Foul	
Pete Alonso walks.

2022-06-16	CH	82.1	1272	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
2-0	Bot 7	Ball	
Pete Alonso walks.

2022-06-16	FF	92.6	2504	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso walks.

2022-06-16	FF	92.4	2556	Boxberger, Brad(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso walks.

2022-06-16	SL	84.4	2566	Ashby, Aaron(L)	Alonso, Pete(R)	53.5	40°	150	
0-0	Bot 1	Hit Into Play	
Pete Alonso pops out softly to shortstop Willy Adames.

2022-06-16	CH	80.3	1784	Milner, Hoby(L)	Alonso, Pete(R)	75.2	66°	126	
2-1	Bot 5	Hit Into Play	
Pete Alonso pops out to shortstop Willy Adames.

2022-06-16	CH	79.9	1678	Milner, Hoby(L)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso pops out to shortstop Willy Adames.

2022-06-16	CH	81.2	1653	Milner, Hoby(L)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Ball	
Pete Alonso pops out to shortstop Willy Adames.

2022-06-16	SI	88.5	1990	Milner, Hoby(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso pops out to shortstop Willy Adames.

2022-06-15	FC	96.1	2690	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
2-2	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-15	FC	97.0	2727	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso strikes out swinging.

2022-06-15	SL	86.0	2892	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-1	Bot 6	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-06-15	FC	95.6	2639	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso strikes out swinging.

2022-06-15	FC	95.6	2705	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-15	SL	85.6	2796	Burnes, Corbin(R)	Alonso, Pete(R)	76.6	88°	33	
2-2	Bot 4	Hit Into Play	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	CH	91.0	1995	Burnes, Corbin(R)	Alonso, Pete(R)	69.1	-29°	5	
2-2	Bot 4	Foul	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	FC	96.2	2760	Burnes, Corbin(R)	Alonso, Pete(R)	78.4	18°	185	
2-2	Bot 4	Foul	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	FC	95.3	2692	Burnes, Corbin(R)	Alonso, Pete(R)	71.2	31°	183	
2-1	Bot 4	Foul	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	FC	94.5	2597	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
2-0	Bot 4	Swinging Strike	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	SI	97.2	2439	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Ball	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	FC	95.5	2597	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso pops out to catcher Victor Caratini in foul territory.

2022-06-15	FC	95.9	2777	Burnes, Corbin(R)	Alonso, Pete(R)	71.4	70°	93	
2-2	Bot 1	Hit Into Play	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	SL	86.8	2800	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	SI	95.9	2500	Burnes, Corbin(R)	Alonso, Pete(R)	64.1	32°	191	
1-2	Bot 1	Foul	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	FC	94.8	2606	Burnes, Corbin(R)	Alonso, Pete(R)	79.6	10°	130	
1-1	Bot 1	Foul	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	CU	83.0	2834	Burnes, Corbin(R)	Alonso, Pete(R)	45.6	-57°	0	
1-0	Bot 1	Foul	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	SI	96.2	2448	Burnes, Corbin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso pops out to first baseman Keston Hiura in foul territory.

2022-06-15	FF	93.8	2437	Strzelecki, Peter(R)	Alonso, Pete(R)	97.7	39°	349	
1-2	Bot 8	Hit Into Play	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-15	CH	86.0	1745	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-2	Bot 8	Ball	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-15	SL	83.8	2999	Strzelecki, Peter(R)	Alonso, Pete(R)	70.2	51°	183	
0-2	Bot 8	Foul	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-15	FF	93.8	2360	Strzelecki, Peter(R)	Alonso, Pete(R)	61.2	31°	64	
0-2	Bot 8	Foul	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-15	FF	92.8	2394	Strzelecki, Peter(R)	Alonso, Pete(R)	72.6	14°	146	
0-1	Bot 8	Foul	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-15	SL	82.4	2928	Strzelecki, Peter(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso flies out to left fielder Andrew McCutchen.

2022-06-14	SI	93.3	2101	Houser, Adrian(R)	Alonso, Pete(R)	107.8	14°	269	
1-1	Bot 5	Hit Into Play	
Pete Alonso singles on a sharp line drive to center fielder Tyrone Taylor. Starling Marte scores.

2022-06-14	SL	84.4	2233	Houser, Adrian(R)	Alonso, Pete(R)	85.1	81°	78	
1-0	Bot 5	Foul	
Pete Alonso singles on a sharp line drive to center fielder Tyrone Taylor. Starling Marte scores.

2022-06-14	SI	93.5	2043	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a sharp line drive to center fielder Tyrone Taylor. Starling Marte scores.

2022-06-14	SI	92.7	1992	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
3-0	Bot 3	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-14	SI	92.7	2095	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
2-0	Bot 3	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-14	SI	92.1	1969	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-14	SI	93.3	2030	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-14	CU	82.0	1878	Houser, Adrian(R)	Alonso, Pete(R)	103.6	10°	223	
1-0	Bot 1	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Christian Yelich. Brandon Nimmo scores. Starling Marte to 3rd.

2022-06-14	SL	86.0	2342	Houser, Adrian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Blocked Ball	
Pete Alonso singles on a sharp line drive to left fielder Christian Yelich. Brandon Nimmo scores. Starling Marte to 3rd.

2022-06-14	CU	78.2	2444	Kelley, Trevor(R)	Alonso, Pete(R)	94.4	38°	323	
0-0	Bot 8	Hit Into Play	
Pete Alonso flies out to center fielder Tyrone Taylor.

2022-06-12	CH	83.0	1601	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
3-1	Top 5	Ball	
Pete Alonso walks. Starling Marte to 2nd.

2022-06-12	FF	92.7	2064	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
2-1	Top 5	Ball	
Pete Alonso walks. Starling Marte to 2nd.

2022-06-12	CH	83.9	1794	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
1-1	Top 5	Ball	
Pete Alonso walks. Starling Marte to 2nd.

2022-06-12	CH	83.0	1690	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Top 5	Swinging Strike	
Pete Alonso walks. Starling Marte to 2nd.

2022-06-12	CU	81.2	3048	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso walks. Starling Marte to 2nd.

2022-06-12	CH	84.3	1708	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
1-2	Top 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-12	FF	93.9	1909	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
0-2	Top 3	Ball	
Pete Alonso strikes out swinging.

2022-06-12	FF	91.9	2053	Sandoval, Patrick(L)	Alonso, Pete(R)	67.8	79°	103	
0-1	Top 3	Foul	
Pete Alonso strikes out swinging.

2022-06-12	CU	79.9	2873	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso strikes out swinging.

2022-06-12	FF	95.2	1987	Sandoval, Patrick(L)	Alonso, Pete(R)	53.8	0°	36	
0-2	Top 1	Hit Into Play	
Pete Alonso grounds out softly, third baseman Anthony Rendon to first baseman Jared Walsh.

2022-06-12	FF	93.7	1966	Sandoval, Patrick(L)	Alonso, Pete(R)	64.3	57°	163	
0-2	Top 1	Foul	
Pete Alonso grounds out softly, third baseman Anthony Rendon to first baseman Jared Walsh.

2022-06-12	CH	84.5	1760	Sandoval, Patrick(L)	Alonso, Pete(R)	102.9	16°	255	
0-2	Top 1	Foul	
Pete Alonso grounds out softly, third baseman Anthony Rendon to first baseman Jared Walsh.

2022-06-12	FF	94.2	2255	Sandoval, Patrick(L)	Alonso, Pete(R)	71.5	16°	156	
0-1	Top 1	Foul	
Pete Alonso grounds out softly, third baseman Anthony Rendon to first baseman Jared Walsh.

2022-06-12	CU	80.1	2867	Sandoval, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso grounds out softly, third baseman Anthony Rendon to first baseman Jared Walsh.

2022-06-12	FF	96.1	2309	Iglesias, Raisel(R)	Alonso, Pete(R)	112.5	21°	414	
2-2	Top 9	Hit Into Play	
Pete Alonso homers (18) on a fly ball to left field.

2022-06-12	FF	96.2	2339	Iglesias, Raisel(R)	Alonso, Pete(R)	76.0	27°	228	
2-1	Top 9	Foul	
Pete Alonso homers (18) on a fly ball to left field.

2022-06-12	FF	95.1	2311	Iglesias, Raisel(R)	Alonso, Pete(R)	--	°		
2-0	Top 9	Called Strike	
Pete Alonso homers (18) on a fly ball to left field.

2022-06-12	FF	94.4	2212	Iglesias, Raisel(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso homers (18) on a fly ball to left field.

2022-06-12	SL	85.9	2596	Iglesias, Raisel(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso homers (18) on a fly ball to left field.

2022-06-12	SI	92.6	2038	Bradley, Archie(R)	Alonso, Pete(R)	62.9	12°	110	
1-0	Top 7	Hit Into Play	
Pete Alonso singles on a ground ball to second baseman Matt Duffy. Starling Marte scores. Pete Alonso to 2nd. Pete Alonso advances to 2nd, on a throwing error by second baseman Matt Duffy.

2022-06-12	SI	92.2	2041	Bradley, Archie(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso singles on a ground ball to second baseman Matt Duffy. Starling Marte scores. Pete Alonso to 2nd. Pete Alonso advances to 2nd, on a throwing error by second baseman Matt Duffy.

2022-06-11	ST	82.9	2533	Lorenzen, Michael(R)	Alonso, Pete(R)	73.3	-32°	4	
2-1	Top 6	Hit Into Play	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso grounds into a force out, shortstop Andrew Velazquez to second baseman Luis Rengifo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-06-11	SI	93.3	2272	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Ball	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso grounds into a force out, shortstop Andrew Velazquez to second baseman Luis Rengifo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-06-11	SI	93.2	1100	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso grounds into a force out, shortstop Andrew Velazquez to second baseman Luis Rengifo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-06-11	ST	81.7	2438	Lorenzen, Michael(R)	Alonso, Pete(R)	102.1	35°	354	
0-0	Top 6	Foul	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso grounds into a force out, shortstop Andrew Velazquez to second baseman Luis Rengifo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-06-11	ST	84.8	2294	Lorenzen, Michael(R)	Alonso, Pete(R)	82.6	1°	48	
1-2	Top 4	Hit Into Play	
Pete Alonso grounds out, first baseman Jared Walsh to pitcher Michael Lorenzen.

2022-06-11	ST	83.0	2358	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso grounds out, first baseman Jared Walsh to pitcher Michael Lorenzen.

2022-06-11	FC	90.3	2504	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Foul	
Pete Alonso grounds out, first baseman Jared Walsh to pitcher Michael Lorenzen.

2022-06-11	SI	94.0	2101	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso grounds out, first baseman Jared Walsh to pitcher Michael Lorenzen.

2022-06-11	SI	94.8	2127	Lorenzen, Michael(R)	Alonso, Pete(R)	99.5	52°	278	
1-0	Top 1	Hit Into Play	
Pete Alonso flies out to left fielder Brandon Marsh.

2022-06-11	ST	84.2	2342	Lorenzen, Michael(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Blocked Ball	
Pete Alonso flies out to left fielder Brandon Marsh.

2022-06-11	CU	83.4	2361	Ortega, Oliver(R)	Alonso, Pete(R)	106.7	34°	401	
0-2	Top 8	Hit Into Play	
Pete Alonso homers (17) on a fly ball to left field.

2022-06-11	FF	98.1	2291	Ortega, Oliver(R)	Alonso, Pete(R)	--	°		
0-2	Top 8	Foul	
Pete Alonso homers (17) on a fly ball to left field.

2022-06-11	CU	82.5	2463	Ortega, Oliver(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Called Strike	
Pete Alonso homers (17) on a fly ball to left field.

2022-06-11	FF	97.1	2176	Ortega, Oliver(R)	Alonso, Pete(R)	76.2	57°	209	
0-0	Top 8	Foul	
Pete Alonso homers (17) on a fly ball to left field.

2022-06-10	FF	93.0	2282	Barria, Jaime(R)	Alonso, Pete(R)	103.8	53°	296	
2-2	Top 9	Hit Into Play	
Pete Alonso flies out sharply to left fielder Brandon Marsh.

2022-06-10	SL	87.4	2301	Barria, Jaime(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso flies out sharply to left fielder Brandon Marsh.

2022-06-10	SI	92.8	2169	Barria, Jaime(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Foul	
Pete Alonso flies out sharply to left fielder Brandon Marsh.

2022-06-10	ST	79.3	2378	Wantz, Andrew(R)	Alonso, Pete(R)	89.7	20°	254	
1-2	Top 5	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Jo Adell.

2022-06-10	FF	93.7	2336	Wantz, Andrew(R)	Alonso, Pete(R)	80.0	73°	131	
1-2	Top 5	Foul	
Pete Alonso singles on a line drive to right fielder Jo Adell.

2022-06-10	CH	84.5	1610	Barria, Jaime(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Called Strike	
Pete Alonso flies out sharply to left fielder Brandon Marsh.

2022-06-10	SI	92.3	2158	Barria, Jaime(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso flies out sharply to left fielder Brandon Marsh.

2022-06-10	ST	81.4	2403	Wantz, Andrew(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso singles on a line drive to right fielder Jo Adell.

2022-06-10	ST	80.9	2381	Wantz, Andrew(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Called Strike	
Pete Alonso singles on a line drive to right fielder Jo Adell.

2022-06-10	FF	93.9	2323	Wantz, Andrew(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso singles on a line drive to right fielder Jo Adell.

2022-06-10	CH	82.4	1938	Diaz, Jhonathan(L)	Alonso, Pete(R)	106.4	1°	62	
1-1	Top 1	Hit Into Play	
Pete Alonso grounds into a double play, second baseman Tyler Wade to first baseman Jared Walsh. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-10	CH	80.0	1673	Diaz, Jhonathan(L)	Alonso, Pete(R)	--	°		
1-0	Top 1	Swinging Strike	
Pete Alonso grounds into a double play, second baseman Tyler Wade to first baseman Jared Walsh. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-10	CU	75.1	2805	Diaz, Jhonathan(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso grounds into a double play, second baseman Tyler Wade to first baseman Jared Walsh. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-06-10	SI	93.5	2136	Bradley, Archie(R)	Alonso, Pete(R)	68.5	55°	175	
0-1	Top 2	Hit Into Play	
Pete Alonso pops out to second baseman Tyler Wade.

2022-06-10	KC	80.6	1898	Bradley, Archie(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso pops out to second baseman Tyler Wade.

2022-06-10	SL	83.9	2194	Barria, Jaime(R)	Alonso, Pete(R)	79.2	82°	44	
0-1	Top 6	Hit Into Play	
Pete Alonso pops out to catcher Max Stassi in foul territory.

2022-06-10	SI	89.3	2242	Barria, Jaime(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso pops out to catcher Max Stassi in foul territory.

2022-06-07	SI	95.7	2337	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Hit By Pitch	
Mets challenged (hit by pitch), call on the field was overturned: Pete Alonso hit by pitch.

2022-06-07	SL	87.5	2862	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Mets challenged (hit by pitch), call on the field was overturned: Pete Alonso hit by pitch.

2022-06-07	SL	88.6	2858	Darvish, Yu(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Mets challenged (hit by pitch), call on the field was overturned: Pete Alonso hit by pitch.

2022-06-06	SL	88.8	2437	Snell, Blake(L)	Alonso, Pete(R)	103.9	2°	64	
0-0	Top 5	Hit Into Play	
Pete Alonso reaches on a throwing error by third baseman Manny Machado.

2022-06-06	SL	89.1	2475	Snell, Blake(L)	Alonso, Pete(R)	--	°		
3-2	Top 3	Foul Tip	
Pete Alonso strikes out on a foul tip.

2022-06-06	SL	87.4	2448	Snell, Blake(L)	Alonso, Pete(R)	--	°		
2-2	Top 3	Blocked Ball	
Pete Alonso strikes out on a foul tip.

2022-06-06	FF	96.1	2447	Snell, Blake(L)	Alonso, Pete(R)	--	°		
1-2	Top 3	Ball	
Pete Alonso strikes out on a foul tip.

2022-06-06	SL	87.2	2471	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-2	Top 3	Blocked Ball	
Pete Alonso strikes out on a foul tip.

2022-06-06	SL	88.9	2410	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-1	Top 3	Swinging Strike	
Pete Alonso strikes out on a foul tip.

2022-06-06	FF	94.1	2438	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso strikes out on a foul tip.

2022-06-06	ST	82.2	2573	Wilson, Steven(R)	Alonso, Pete(R)	76.4	68°	105	
1-2	Top 7	Hit Into Play	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	FF	97.3	2172	Wilson, Steven(R)	Alonso, Pete(R)	--	°		
0-2	Top 7	Ball	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	ST	81.5	2724	Wilson, Steven(R)	Alonso, Pete(R)	67.0	71°	127	
0-2	Top 7	Foul	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	ST	81.5	2657	Wilson, Steven(R)	Alonso, Pete(R)	72.1	60°	174	
0-2	Top 7	Foul	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	ST	83.9	2596	Wilson, Steven(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Foul	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	FC	88.7	2332	Stammen, Craig(R)	Alonso, Pete(R)	100.3	7°	149	
0-0	Top 9	Hit Into Play	
Pete Alonso singles on a sharp line drive to right fielder Nomar Mazara.

2022-06-06	ST	80.7	2673	Wilson, Steven(R)	Alonso, Pete(R)	83.4	-24°	6	
0-0	Top 7	Foul	
Pete Alonso pops out to first baseman Eric Hosmer.

2022-06-06	FF	96.5	2624	Snell, Blake(L)	Alonso, Pete(R)	--	°		
3-1	Top 1	Ball	
Pete Alonso walks.

2022-06-06	FF	95.6	2510	Snell, Blake(L)	Alonso, Pete(R)	--	°		
2-1	Top 1	Ball	
Pete Alonso walks.

2022-06-06	FF	95.9	2531	Snell, Blake(L)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso walks.

2022-06-06	CU	80.5	2569	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-1	Top 1	Blocked Ball	
Pete Alonso walks.

2022-06-06	CU	79.6	2500	Snell, Blake(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Swinging Strike Blocked	
Pete Alonso walks.

2022-06-05	FF	92.0	2467	Urías, Julio(L)	Alonso, Pete(R)	65.1	65°	124	
2-1	Top 6	Hit Into Play	
Pete Alonso pops out to first baseman Freddie Freeman in foul territory.

2022-06-05	CH	85.9	2084	Urías, Julio(L)	Alonso, Pete(R)	94.8	-19°	7	
2-0	Top 6	Foul	
Pete Alonso pops out to first baseman Freddie Freeman in foul territory.

2022-06-05	CH	84.8	1895	Urías, Julio(L)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso pops out to first baseman Freddie Freeman in foul territory.

2022-06-05	FF	93.5	2482	Urías, Julio(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso pops out to first baseman Freddie Freeman in foul territory.

2022-06-05	SV	80.4	2921	Urías, Julio(L)	Alonso, Pete(R)	93.5	40°	309	
3-1	Top 3	Hit Into Play	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	CH	86.1	1908	Urías, Julio(L)	Alonso, Pete(R)	--	°		
2-1	Top 3	Ball	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	SV	80.5	2952	Urías, Julio(L)	Alonso, Pete(R)	--	°		
2-0	Top 3	Called Strike	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	FF	92.2	2670	Urías, Julio(L)	Alonso, Pete(R)	--	°		
1-0	Top 3	Ball	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	SV	81.6	2966	Urías, Julio(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	FF	90.4	2434	Urías, Julio(L)	Alonso, Pete(R)	83.2	50°	227	
0-0	Top 1	Hit Into Play	
Pete Alonso flies out to left fielder Chris Taylor.

2022-06-05	KC	86.9	2569	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-05	SL	89.1	2325	Graterol, Brusdar(R)	Alonso, Pete(R)	111.4	18°	338	
0-0	Top 8	Hit Into Play	
Pete Alonso doubles (9) on a sharp line drive to left fielder Chris Taylor. Francisco Lindor scores.

2022-06-05	FF	96.8	2265	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
0-2	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-05	FF	97.4	2331	Kimbrel, Craig(R)	Alonso, Pete(R)	80.9	20°	209	
0-2	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-06-05	FF	96.9	2293	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-06-05	FF	97.6	2311	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-04	SL	85.3	2768	Buehler, Walker(R)	Alonso, Pete(R)	109.4	22°	401	
1-1	Top 3	Hit Into Play	
Pete Alonso homers (15) on a fly ball to left field. Starling Marte scores.

2022-06-04	FF	95.9	2457	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
0-1	Top 3	Ball	
Pete Alonso homers (15) on a fly ball to left field. Starling Marte scores.

2022-06-04	SL	84.6	2775	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Swinging Strike	
Pete Alonso homers (15) on a fly ball to left field. Starling Marte scores.

2022-06-04	SL	84.7	2545	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-04	SL	84.8	2564	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-06-04	FF	95.3	2156	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-06-04	FF	95.8	2249	Buehler, Walker(R)	Alonso, Pete(R)	78.6	20°	205	
1-0	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-06-04	FC	92.2	2365	Buehler, Walker(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-06-04	ST	85.5	2316	Almonte, Yency(R)	Alonso, Pete(R)	--	°		
2-2	Top 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-04	ST	85.8	2382	Almonte, Yency(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-06-04	ST	84.9	2643	Phillips, Evan(R)	Alonso, Pete(R)	100.7	12°	262	
2-1	Top 9	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Chris Taylor.

2022-06-04	ST	85.1	2464	Phillips, Evan(R)	Alonso, Pete(R)	--	°		
2-0	Top 9	Called Strike	
Pete Alonso singles on a sharp line drive to left fielder Chris Taylor.

2022-06-04	SI	99.9	2077	Graterol, Brusdar(R)	Alonso, Pete(R)	109.0	19°	394	
1-0	Top 7	Hit Into Play	
Pete Alonso homers (16) on a line drive to center field. Brandon Nimmo scores. Starling Marte scores.

2022-06-04	ST	83.4	2345	Almonte, Yency(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-06-04	SI	100.1	1973	Graterol, Brusdar(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso homers (16) on a line drive to center field. Brandon Nimmo scores. Starling Marte scores.

2022-06-04	SI	96.8	2049	Almonte, Yency(R)	Alonso, Pete(R)	74.8	45°	213	
0-1	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-06-04	FF	96.4	2401	Phillips, Evan(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso singles on a sharp line drive to left fielder Chris Taylor.

2022-06-04	ST	86.1	2579	Phillips, Evan(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso singles on a sharp line drive to left fielder Chris Taylor.

2022-06-04	ST	86.0	2339	Almonte, Yency(R)	Alonso, Pete(R)	67.2	36°	155	
0-0	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-06-03	CH	81.6	2004	Anderson, Tyler(L)	Alonso, Pete(R)	91.5	4°	75	
2-2	Top 4	Hit Into Play	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	FF	92.7	2380	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
1-2	Top 4	Ball	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	FF	92.8	2244	Anderson, Tyler(L)	Alonso, Pete(R)	52.0	40°	135	
1-2	Top 4	Foul	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	CH	81.1	1973	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
0-2	Top 4	Ball	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	CH	80.9	1927	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
0-1	Top 4	Swinging Strike	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	CH	80.9	1892	Anderson, Tyler(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Swinging Strike	
Pete Alonso grounds out, third baseman Justin Turner to first baseman Freddie Freeman.

2022-06-03	FC	89.0	2421	Anderson, Tyler(L)	Alonso, Pete(R)	59.1	87°	45	
0-2	Top 2	Hit Into Play	
Pete Alonso pops out softly to catcher Will Smith in foul territory.

2022-06-03	CH	79.1	1829	Anderson, Tyler(L)	Alonso, Pete(R)	46.6	-29°	3	
0-2	Top 2	Foul	
Pete Alonso pops out softly to catcher Will Smith in foul territory.

2022-06-03	FF	90.7	2212	Anderson, Tyler(L)	Alonso, Pete(R)	64.8	36°	197	
0-1	Top 2	Foul	
Pete Alonso pops out softly to catcher Will Smith in foul territory.

2022-06-03	FF	90.8	2145	Anderson, Tyler(L)	Alonso, Pete(R)	67.0	31°	194	
0-0	Top 2	Foul	
Pete Alonso pops out softly to catcher Will Smith in foul territory.

2022-06-03	FF	97.5	2399	Hudson, Daniel(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-03	FF	96.0	2344	Hudson, Daniel(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-06-03	FF	97.3	2446	Hudson, Daniel(R)	Alonso, Pete(R)	72.2	36°	230	
2-0	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-06-03	SL	87.1	2669	Hudson, Daniel(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-03	SL	88.9	2521	Hudson, Daniel(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-03	SI	96.8	2023	Almonte, Yency(R)	Alonso, Pete(R)	111.6	33°	433	
0-0	Top 7	Hit Into Play	
Pete Alonso homers (14) on a fly ball to left center field.

2022-06-02	SL	87.5	2514	Gonsolin, Tony(R)	Alonso, Pete(R)	81.6	-19°	7	
0-1	Top 4	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Trea Turner to second baseman Gavin Lux. Luis Guillorme out at 2nd. Pete Alonso to 1st.

2022-06-02	FS	83.3	1530	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Swinging Strike	
Pete Alonso grounds into a force out, shortstop Trea Turner to second baseman Gavin Lux. Luis Guillorme out at 2nd. Pete Alonso to 1st.

2022-06-02	FS	83.5	1330	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
3-2	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-02	FS	84.1	1500	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-06-02	SL	88.0	2485	Gonsolin, Tony(R)	Alonso, Pete(R)	79.5	43°	257	
2-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-06-02	SL	88.4	2385	Gonsolin, Tony(R)	Alonso, Pete(R)	46.2	-24°	5	
2-1	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-06-02	FF	91.4	2350	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-06-02	FF	96.7	2265	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-02	FF	93.3	2419	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Pete Alonso strikes out swinging.

2022-06-02	CU	79.5	2490	Gonsolin, Tony(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-06-02	FF	97.0	2345	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-06-02	KC	86.4	2626	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-02	KC	86.0	2660	Kimbrel, Craig(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-06-02	FF	97.0	2249	Kimbrel, Craig(R)	Alonso, Pete(R)	81.1	10°	138	
0-0	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-06-02	SL	93.1	2474	Graterol, Brusdar(R)	Alonso, Pete(R)	--	°		
1-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-06-02	SI	101.4	1960	Graterol, Brusdar(R)	Alonso, Pete(R)	93.0	25°	295	
1-1	Top 7	Foul	
Pete Alonso strikes out swinging.

2022-06-02	SI	100.9	2044	Graterol, Brusdar(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-06-02	SI	100.8	2138	Graterol, Brusdar(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-06-01	CU	81.1	2751	Lee, Evan(L)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Hit By Pitch	
Pete Alonso hit by pitch.

2022-06-01	FF	92.1	2421	Lee, Evan(L)	Alonso, Pete(R)	100.3	31°	332	
3-1	Bot 3	Foul	
Pete Alonso hit by pitch.

2022-06-01	FF	91.2	2466	Lee, Evan(L)	Alonso, Pete(R)	--	°		
2-1	Bot 3	Ball	
Pete Alonso hit by pitch.

2022-06-01	CU	80.1	2758	Lee, Evan(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso hit by pitch.

2022-06-01	FF	90.7	2439	Lee, Evan(L)	Alonso, Pete(R)	64.3	43°	164	
1-0	Bot 3	Foul	
Pete Alonso hit by pitch.

2022-06-01	FF	91.1	2468	Lee, Evan(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso hit by pitch.

2022-06-01	FF	91.5	2357	Lee, Evan(L)	Alonso, Pete(R)	--	°		
3-0	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-01	FF	92.4	2265	Lee, Evan(L)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-01	FF	90.5	2192	Lee, Evan(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-01	FF	92.6	2420	Lee, Evan(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-06-01	SI	93.8	2121	Arano, Víctor(R)	Alonso, Pete(R)	83.3	23°	275	
1-1	Bot 5	Hit Into Play	
Pete Alonso lines out to left fielder Yadiel Hernandez.

2022-06-01	SI	92.8	2072	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Foul	
Pete Alonso lines out to left fielder Yadiel Hernandez.

2022-06-01	SI	96.3	2112	Finnegan, Kyle(R)	Alonso, Pete(R)	68.7	67°	111	
0-0	Bot 7	Hit Into Play	
Pete Alonso pops out to first baseman Josh Bell in foul territory.

2022-06-01	SI	93.4	2089	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso lines out to left fielder Yadiel Hernandez.

2022-05-31	SL	84.0	2270	Corbin, Patrick(L)	Alonso, Pete(R)	109.0	5°	124	
0-0	Bot 3	Hit Into Play	
Pete Alonso singles on a sharp ground ball to left fielder Dee Strange-Gordon.

2022-05-31	SI	93.7	2045	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-31	CU	79.8	2594	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-05-31	SL	84.3	2342	Corbin, Patrick(L)	Alonso, Pete(R)	103.1	-6°	22	
3-2	Bot 1	Foul	
Pete Alonso walks.

2022-05-31	FC	86.9	2351	Ramírez, Erasmo(R)	Alonso, Pete(R)	70.4	9°	100	
2-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-05-31	SI	94.3	2112	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-31	SL	85.0	2285	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-31	FF	91.9	2182	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
1-2	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-05-31	CU	83.0	2162	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
3-2	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-31	SL	84.7	2259	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-31	FF	93.0	2242	Ramírez, Erasmo(R)	Alonso, Pete(R)	75.3	16°	168	
1-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-05-31	SL	87.4	2130	Weems, Jordan(R)	Alonso, Pete(R)	114.7	19°	365	
3-2	Bot 7	Foul	
Pete Alonso strikes out swinging.

2022-05-31	SI	92.8	2079	Corbin, Patrick(L)	Alonso, Pete(R)	73.3	44°	211	
0-1	Bot 1	Foul	
Pete Alonso walks.

2022-05-31	SI	91.8	2118	Ramírez, Erasmo(R)	Alonso, Pete(R)	108.8	6°	120	
1-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-05-31	FF	97.1	2124	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 7	Ball	
Pete Alonso strikes out swinging.

2022-05-31	SL	84.2	2422	Corbin, Patrick(L)	Alonso, Pete(R)	80.6	-31°	2	
0-0	Bot 1	Foul	
Pete Alonso walks.

2022-05-31	FC	89.3	2362	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-2	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-05-31	FC	89.1	2483	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-31	SL	87.8	2199	Weems, Jordan(R)	Alonso, Pete(R)	72.7	10°	102	
2-1	Bot 7	Foul	
Pete Alonso strikes out swinging.

2022-05-31	FF	96.3	2262	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
2-0	Bot 7	Called Strike	
Pete Alonso strikes out swinging.

2022-05-31	FC	90.1	2383	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-31	FF	94.9	1986	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso strikes out swinging.

2022-05-31	SL	85.9	2135	Weems, Jordan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso strikes out swinging.

2022-05-30	FC	89.4	2180	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-30	CU	80.4	2592	Fedde, Erick(R)	Alonso, Pete(R)	55.9	-51°	1	
3-2	Bot 1	Foul	
Pete Alonso walks.

2022-05-30	FC	89.6	2100	Fedde, Erick(R)	Alonso, Pete(R)	73.3	39°	210	
3-2	Bot 1	Foul	
Pete Alonso walks.

2022-05-30	SI	93.1	1710	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-30	CU	79.2	2536	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Blocked Ball	
Pete Alonso walks.

2022-05-30	FC	90.4	2075	Fedde, Erick(R)	Alonso, Pete(R)	77.8	36°	251	
1-2	Bot 1	Foul	
Pete Alonso walks.

2022-05-30	ST	79.2	2722	Espino, Paolo(R)	Alonso, Pete(R)	80.9	34°	296	
3-2	Bot 5	Hit Into Play	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	FC	91.0	2215	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-30	ST	77.8	2669	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
3-1	Bot 5	Swinging Strike	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	FF	88.5	2246	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
3-0	Bot 5	Called Strike	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	CU	79.6	2507	Fedde, Erick(R)	Alonso, Pete(R)	62.4	67°	127	
0-1	Bot 1	Foul	
Pete Alonso walks.

2022-05-30	CU	79.7	2487	Fedde, Erick(R)	Alonso, Pete(R)	80.3	52°	224	
0-0	Bot 1	Foul	
Pete Alonso walks.

2022-05-30	ST	77.4	2760	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
2-0	Bot 5	Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	ST	78.3	2914	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Blocked Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	CU	71.1	3034	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso flies out to center fielder Victor Robles.

2022-05-30	SI	95.1	2049	Machado, Andrés(R)	Alonso, Pete(R)	59.0	86°	40	
2-2	Bot 2	Hit Into Play	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	FF	96.3	2191	Machado, Andrés(R)	Alonso, Pete(R)	81.4	37°	254	
2-2	Bot 2	Foul	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	FF	95.1	2153	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
1-2	Bot 2	Ball	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	SL	86.0	1995	Machado, Andrés(R)	Alonso, Pete(R)	100.6	29°	351	
1-2	Bot 2	Foul	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	FF	94.6	2420	Voth, Austin(R)	Alonso, Pete(R)	50.4	27°	134	
0-2	Bot 3	Hit Into Play	
Pete Alonso pops out softly to shortstop Alcides Escobar.

2022-05-30	CU	78.9	3205	Voth, Austin(R)	Alonso, Pete(R)	57.7	56°	134	
0-2	Bot 3	Foul	
Pete Alonso pops out softly to shortstop Alcides Escobar.

2022-05-30	SL	87.4	1962	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-2	Bot 2	Blocked Ball	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	CH	86.0	1400	Rogers, Josh(L)	Alonso, Pete(R)	107.8	30°	417	
0-1	Bot 8	Hit Into Play	
Pete Alonso homers (13) on a fly ball to center field.

2022-05-30	FF	94.5	2362	Voth, Austin(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Foul Tip	
Pete Alonso pops out softly to shortstop Alcides Escobar.

2022-05-30	SL	86.2	2049	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-1	Bot 2	Swinging Strike	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-30	FF	90.6	1965	Rogers, Josh(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso homers (13) on a fly ball to center field.

2022-05-30	CU	77.9	3116	Voth, Austin(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso pops out softly to shortstop Alcides Escobar.

2022-05-30	SL	85.6	2012	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Called Strike	
Pete Alonso pops out to catcher Keibert Ruiz in foul territory.

2022-05-29	SL	91.4	2517	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Blocked Ball	
Pete Alonso walks.

2022-05-29	FF	97.7	2531	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Ball	
Pete Alonso walks.

2022-05-29	SL	90.2	2415	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso walks.

2022-05-29	SI	95.9	2198	Wheeler, Zack(R)	Alonso, Pete(R)	66.6	38°	171	
1-1	Bot 3	Foul	
Pete Alonso walks.

2022-05-29	SI	97.1	2218	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso walks.

2022-05-29	SI	95.2	2155	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso walks.

2022-05-29	SL	90.2	2546	Wheeler, Zack(R)	Alonso, Pete(R)	70.5	50°	189	
1-2	Bot 1	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Nick Castellanos. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-05-29	SL	91.5	2541	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Foul Tip	
Pete Alonso singles on a fly ball to right fielder Nick Castellanos. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-05-29	SI	96.8	2253	Wheeler, Zack(R)	Alonso, Pete(R)	74.5	54°	193	
1-0	Bot 1	Foul	
Pete Alonso singles on a fly ball to right fielder Nick Castellanos. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-05-29	SL	91.6	2445	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso singles on a fly ball to right fielder Nick Castellanos. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-05-29	SL	89.2	2113	Familia, Jeurys(R)	Alonso, Pete(R)	96.4	3°	72	
2-1	Bot 7	Hit Into Play	
Pete Alonso grounds into a force out, third baseman Alec Bohm to second baseman Jean Segura. Luis Guillorme out at 2nd.

2022-05-29	SI	96.2	2217	Familia, Jeurys(R)	Alonso, Pete(R)	74.7	-48°	1	
2-0	Bot 7	Foul	
Pete Alonso grounds into a force out, third baseman Alec Bohm to second baseman Jean Segura. Luis Guillorme out at 2nd.

2022-05-29	SI	95.4	2199	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso grounds into a force out, third baseman Alec Bohm to second baseman Jean Segura. Luis Guillorme out at 2nd.

2022-05-29	SI	95.3	2191	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso grounds into a force out, third baseman Alec Bohm to second baseman Jean Segura. Luis Guillorme out at 2nd.

2022-05-28	SI	93.2	2049	Eflin, Zach(R)	Alonso, Pete(R)	101.1	18°	316	
2-1	Bot 5	Hit Into Play	
Pete Alonso out on a sacrifice fly to left fielder Kyle Schwarber. Francisco Lindor scores.

2022-05-28	CU	80.3	2461	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Blocked Ball	
Pete Alonso out on a sacrifice fly to left fielder Kyle Schwarber. Francisco Lindor scores.

2022-05-28	SI	93.3	2143	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Called Strike	
Pete Alonso out on a sacrifice fly to left fielder Kyle Schwarber. Francisco Lindor scores.

2022-05-28	SI	92.6	2079	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso out on a sacrifice fly to left fielder Kyle Schwarber. Francisco Lindor scores.

2022-05-28	CU	77.7	2377	Eflin, Zach(R)	Alonso, Pete(R)	72.9	21°	183	
0-2	Bot 4	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Odubel Herrera. Francisco Lindor to 3rd.

2022-05-28	CU	77.5	2399	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Swinging Strike	
Pete Alonso singles on a line drive to center fielder Odubel Herrera. Francisco Lindor to 3rd.

2022-05-28	SI	93.3	1991	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso singles on a line drive to center fielder Odubel Herrera. Francisco Lindor to 3rd.

2022-05-28	FS	90.9	1270	Norwood, James(R)	Alonso, Pete(R)	104.7	41°	348	
1-0	Bot 7	Hit Into Play	
Pete Alonso flies out sharply to center fielder Odubel Herrera. Starling Marte to 3rd.

2022-05-28	SL	87.0	2029	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso flies out sharply to center fielder Odubel Herrera. Starling Marte to 3rd.

2022-05-28	SI	92.7	1950	Eflin, Zach(R)	Alonso, Pete(R)	52.0	14°	87	
0-0	Bot 1	Hit Into Play	
Pete Alonso grounds out softly, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-27	SL	81.8	1925	Falter, Bailey(L)	Alonso, Pete(R)	104.8	31°	400	
1-0	Bot 3	Hit Into Play	
Pete Alonso homers (12) on a fly ball to left field. Francisco Lindor scores.

2022-05-27	CU	72.9	1853	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso homers (12) on a fly ball to left field. Francisco Lindor scores.

2022-05-27	FF	95.4	2017	Nelson, Nick(R)	Alonso, Pete(R)	109.3	20°	360	
0-2	Bot 4	Hit Into Play	
Pete Alonso doubles (8) on a sharp line drive to right fielder Nick Castellanos. Francisco Lindor scores.

2022-05-27	SL	87.8	2150	Nelson, Nick(R)	Alonso, Pete(R)	74.0	22°	210	
0-1	Bot 4	Foul	
Pete Alonso doubles (8) on a sharp line drive to right fielder Nick Castellanos. Francisco Lindor scores.

2022-05-27	FF	96.2	2035	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso doubles (8) on a sharp line drive to right fielder Nick Castellanos. Francisco Lindor scores.

2022-05-27	SI	92.4	1940	Falter, Bailey(L)	Alonso, Pete(R)	93.1	53°	246	
1-2	Bot 1	Hit Into Play	
Pete Alonso out on a sacrifice fly to right fielder Nick Castellanos. Brandon Nimmo scores. Starling Marte to 3rd.

2022-05-27	SL	84.4	2003	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Blocked Ball	
Pete Alonso out on a sacrifice fly to right fielder Nick Castellanos. Brandon Nimmo scores. Starling Marte to 3rd.

2022-05-27	SI	92.8	1905	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Called Strike	
Pete Alonso out on a sacrifice fly to right fielder Nick Castellanos. Brandon Nimmo scores. Starling Marte to 3rd.

2022-05-27	SI	92.0	1784	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso out on a sacrifice fly to right fielder Nick Castellanos. Brandon Nimmo scores. Starling Marte to 3rd.

2022-05-25	SL	85.7	2742	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
2-2	Top 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-25	SL	85.2	2448	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-05-25	SL	84.6	2546	Junis, Jakob(R)	Alonso, Pete(R)	65.5	41°	167	
1-2	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-05-25	SL	85.3	2530	Junis, Jakob(R)	Alonso, Pete(R)	60.7	36°	128	
1-1	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-05-25	SL	84.5	2471	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-25	SL	83.0	2484	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-05-25	SL	83.4	2504	Junis, Jakob(R)	Alonso, Pete(R)	106.7	0°	39	
2-1	Top 4	Hit Into Play	
Pete Alonso grounds out sharply, second baseman Thairo Estrada to first baseman Wilmer Flores.

2022-05-25	SL	83.1	2461	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso grounds out sharply, second baseman Thairo Estrada to first baseman Wilmer Flores.

2022-05-25	SL	82.2	2430	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Called Strike	
Pete Alonso grounds out sharply, second baseman Thairo Estrada to first baseman Wilmer Flores.

2022-05-25	SL	81.2	2366	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso grounds out sharply, second baseman Thairo Estrada to first baseman Wilmer Flores.

2022-05-25	SL	84.2	2656	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
3-2	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-25	CH	83.6	1384	Junis, Jakob(R)	Alonso, Pete(R)	114.4	17°	305	
3-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-05-25	CH	82.8	2674	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-05-25	SL	83.6	2436	Junis, Jakob(R)	Alonso, Pete(R)	69.9	5°	63	
2-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-05-25	SL	83.6	2392	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
1-2	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-05-25	SL	83.4	2506	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
0-2	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-05-25	SL	82.4	2530	Junis, Jakob(R)	Alonso, Pete(R)	67.7	9°	89	
0-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-05-25	SL	87.1	2368	Littell, Zack(R)	Alonso, Pete(R)	80.2	23°	273	
1-2	Top 8	Hit Into Play	
Pete Alonso lines out to center fielder Stuart Fairchild.

2022-05-25	SL	82.0	2481	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
0-1	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-25	SL	87.3	2356	Littell, Zack(R)	Alonso, Pete(R)	76.7	76°	138	
1-1	Top 8	Foul	
Pete Alonso lines out to center fielder Stuart Fairchild.

2022-05-25	SL	79.4	2365	Junis, Jakob(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-25	SL	88.4	2349	Littell, Zack(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Swinging Strike	
Pete Alonso lines out to center fielder Stuart Fairchild.

2022-05-25	SL	89.1	2380	Littell, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso lines out to center fielder Stuart Fairchild.

2022-05-24	CH	85.2	1459	Webb, Logan(R)	Alonso, Pete(R)	110.1	0°	51	
0-0	Top 5	Hit Into Play	
Pete Alonso grounds out sharply, shortstop Brandon Crawford to first baseman Darin Ruf.

2022-05-24	SL	82.3	2772	Webb, Logan(R)	Alonso, Pete(R)	--	°		
2-2	Top 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-24	SL	81.9	2692	Webb, Logan(R)	Alonso, Pete(R)	77.9	17°	384	
2-2	Top 3	Foul	
Pete Alonso strikes out swinging.

2022-05-24	SI	93.7		Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Ball	
Pete Alonso strikes out swinging.

2022-05-24	CH	85.6	1457	Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-1	Top 3	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-24	SI	91.6	1865	Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-0	Top 3	Called Strike	
Pete Alonso strikes out swinging.

2022-05-24	CH	86.6	1469	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso strikes out swinging.

2022-05-24	SL	82.3	2691	Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-24	SI	92.6	1923	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-05-24	SL	83.2	2665	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-24	SI	93.3	1976	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-05-24	FC	90.5	2410	Leone, Dominic(R)	Alonso, Pete(R)	87.5	65°	147	
0-2	Top 7	Hit Into Play	
Pete Alonso pops out to third baseman Kevin Padlo in foul territory.

2022-05-24	FC	91.5	2409	Leone, Dominic(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Swinging Strike	
Pete Alonso pops out to third baseman Kevin Padlo in foul territory.

2022-05-24	FC	91.5	2441	Leone, Dominic(R)	Alonso, Pete(R)	--	°	0	
0-0	Top 7	Foul Tip	
Pete Alonso pops out to third baseman Kevin Padlo in foul territory.

2022-05-24	SL	88.9	2708	Doval, Camilo(R)	Alonso, Pete(R)	106.7	19°	366	
1-0	Top 8	Hit Into Play	
Pete Alonso out on a sacrifice fly to center fielder Mike Yastrzemski. Francisco Lindor scores.

2022-05-24	FC	100.1	2617	Doval, Camilo(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso out on a sacrifice fly to center fielder Mike Yastrzemski. Francisco Lindor scores.

2022-05-23	FS	91.8	1891	Cobb, Alex(R)	Alonso, Pete(R)	86.3	-1°	27	
1-2	Top 5	Hit Into Play	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	FS	90.6	1868	Cobb, Alex(R)	Alonso, Pete(R)	82.5	-26°	2	
1-2	Top 5	Foul	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	SI	94.9	2282	Cobb, Alex(R)	Alonso, Pete(R)	82.2	44°	236	
1-2	Top 5	Foul	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	SI	95.2	2133	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
0-2	Top 5	Ball	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	FS	91.9	1910	Cobb, Alex(R)	Alonso, Pete(R)	74.7	-26°	3	
0-1	Top 5	Foul	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	SI	94.3	2251	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso grounds out, third baseman Evan Longoria to first baseman Kevin Padlo.

2022-05-23	KC	84.8	2758	Cobb, Alex(R)	Alonso, Pete(R)	106.9	36°	391	
0-0	Top 3	Hit Into Play	
Pete Alonso homers (11) on a fly ball to center field. Starling Marte scores. Francisco Lindor scores.

2022-05-23	SI	94.6	2125	Cobb, Alex(R)	Alonso, Pete(R)	112.9	6°	121	
3-1	Top 2	Hit Into Play	
Pete Alonso singles on a ground ball to shortstop Brandon Crawford.

2022-05-23	SI	94.4	2077	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
3-0	Top 2	Called Strike	
Pete Alonso singles on a ground ball to shortstop Brandon Crawford.

2022-05-23	SI	95.1	2125	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
2-0	Top 2	Ball	
Pete Alonso singles on a ground ball to shortstop Brandon Crawford.

2022-05-23	FS	89.3	1411	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso singles on a ground ball to shortstop Brandon Crawford.

2022-05-23	KC	83.9	2609	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso singles on a ground ball to shortstop Brandon Crawford.

2022-05-23	EP	44.9	786	González, Luis(L)	Alonso, Pete(R)	101.1	4°	80	
0-0	Top 9	Hit Into Play	
Pete Alonso grounds out, second baseman Tommy La Stella to first baseman Wilmer Flores.

2022-05-23	SI	94.8	2003	Llovera, Mauricio(R)	Alonso, Pete(R)	64.9	-24°	6	
0-0	Top 8	Hit Into Play	
Pete Alonso singles on a ground ball to second baseman Tommy La Stella.

2022-05-22	FF	91.7	2239	Gomber, Austin(L)	Alonso, Pete(R)	72.1	-7°	16	
0-0	Top 6	Hit Into Play	
Pete Alonso grounds out to first baseman Connor Joe. Francisco Lindor scores. Jeff McNeil to 3rd.

2022-05-22	CH	83.6	1644	Gomber, Austin(L)	Alonso, Pete(R)	104.6	0°	48	
1-0	Top 4	Hit Into Play	
Pete Alonso grounds into a double play, third baseman Ryan McMahon to second baseman Brendan Rodgers to first baseman Connor Joe. Jeff McNeil out at 2nd. Pete Alonso out at 1st.

2022-05-22	CH	83.4	1692	Gomber, Austin(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Blocked Ball	
Pete Alonso grounds into a double play, third baseman Ryan McMahon to second baseman Brendan Rodgers to first baseman Connor Joe. Jeff McNeil out at 2nd. Pete Alonso out at 1st.

2022-05-22	FF	90.9	2132	Gomber, Austin(L)	Alonso, Pete(R)	82.0	-9°	12	
1-1	Top 2	Hit Into Play	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman Connor Joe.

2022-05-22	FF	89.1	1958	Gomber, Austin(L)	Alonso, Pete(R)	--	°		
0-1	Top 2	Ball	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman Connor Joe.

2022-05-22	FF	89.4	2093	Gomber, Austin(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso grounds out, second baseman Brendan Rodgers to first baseman Connor Joe.

2022-05-22	SL	91.2	2453	Kinley, Tyler(R)	Alonso, Pete(R)	--	°		
0-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-22	SL	89.7	2404	Kinley, Tyler(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-05-22	SL	89.4	2236	Kinley, Tyler(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-21	KC	87.1	2632	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
3-2	Top 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-21	FF	97.7	2297	Márquez, Germán(R)	Alonso, Pete(R)	64.2	-53°	2	
3-2	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-05-21	SL	88.4	2490	Márquez, Germán(R)	Alonso, Pete(R)	62.2	-69°	1	
3-2	Top 5	Foul	
Pete Alonso strikes out swinging.

2022-05-21	KC	87.9	2613	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
2-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-05-21	FF	98.2	2132	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
1-2	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-05-21	KC	87.8	2650	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
1-1	Top 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-21	FF	97.1	2145	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso strikes out swinging.

2022-05-21	SL	85.9	2420	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso strikes out swinging.

2022-05-21	FF	95.7	2134	Márquez, Germán(R)	Alonso, Pete(R)	90.1	-43°	3	
1-1	Top 2	Hit Into Play	
Pete Alonso grounds out, third baseman Ryan McMahon to first baseman C. J. Cron.

2022-05-21	SL	88.4	2481	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Pete Alonso grounds out, third baseman Ryan McMahon to first baseman C. J. Cron.

2022-05-21	CH	80.6	1937	Blach, Ty(L)	Alonso, Pete(R)	98.2	15°	305	
0-1	Top 3	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Randal Grichuk.

2022-05-21	FF	96.2	2194	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso grounds out, third baseman Ryan McMahon to first baseman C. J. Cron.

2022-05-21	CU	78.6	2355	Blach, Ty(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso singles on a line drive to center fielder Randal Grichuk.

2022-05-21	FF	90.2	2009	Goudeau, Ashton(R)	Alonso, Pete(R)	101.0	9°	183	
0-0	Top 5	Hit Into Play	
Pete Alonso grounds out sharply, second baseman Brendan Rodgers to first baseman C. J. Cron.

2022-05-21	CH	80.2	1708	Blach, Ty(L)	Alonso, Pete(R)	107.3	10°	201	
0-0	Top 1	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Sam Hilliard. Francisco Lindor to 2nd.

2022-05-21	FF	94.7	2012	Márquez, Germán(R)	Alonso, Pete(R)	77.8	66°	138	
1-1	Top 1	Hit Into Play	
Pete Alonso pops out to first baseman C. J. Cron.

2022-05-21	SL	86.7	2440	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Called Strike	
Pete Alonso pops out to first baseman C. J. Cron.

2022-05-21	FF	95.6	2049	Márquez, Germán(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso pops out to first baseman C. J. Cron.

2022-05-21	FF	96.2	2284	Estévez, Carlos(R)	Alonso, Pete(R)	81.9	30°	296	
1-2	Top 9	Hit Into Play	
Pete Alonso doubles (7) on a fly ball to left fielder Kris Bryant.

2022-05-21	FF	96.9	2281	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Swinging Strike	
Pete Alonso doubles (7) on a fly ball to left fielder Kris Bryant.

2022-05-21	SL	88.0	618	Estévez, Carlos(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso doubles (7) on a fly ball to left fielder Kris Bryant.

2022-05-21	FC	89.2	2083	Colomé, Alex(R)	Alonso, Pete(R)	73.7	3°	57	
0-2	Top 8	Hit Into Play	
Pete Alonso grounds out, shortstop Garrett Hampson to first baseman C. J. Cron.

2022-05-21	FF	97.1	2261	Estévez, Carlos(R)	Alonso, Pete(R)	81.8	9°	130	
0-0	Top 9	Foul	
Pete Alonso doubles (7) on a fly ball to left fielder Kris Bryant.

2022-05-21	FC	88.6	2042	Colomé, Alex(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Swinging Strike	
Pete Alonso grounds out, shortstop Garrett Hampson to first baseman C. J. Cron.

2022-05-21	SI	93.0	2294	Chacín, Jhoulys(R)	Alonso, Pete(R)	70.1	52°	186	
0-0	Top 7	Hit Into Play	
Pete Alonso singles on a fly ball to first baseman C. J. Cron.

2022-05-21	FC	89.2	1956	Colomé, Alex(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso grounds out, shortstop Garrett Hampson to first baseman C. J. Cron.

2022-05-19	SI	92.0	1951	Hudson, Dakota(R)	Alonso, Pete(R)	90.5	-12°	9	
1-2	Bot 3	Hit Into Play	
Pete Alonso grounds into a double play, third baseman Nolan Arenado to second baseman Tommy Edman to first baseman Albert Pujols. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-05-19	FF	92.1	2149	Hudson, Dakota(R)	Alonso, Pete(R)	--	°		
0-2	Bot 3	Ball	
Pete Alonso grounds into a double play, third baseman Nolan Arenado to second baseman Tommy Edman to first baseman Albert Pujols. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-05-19	FF	92.0	2023	Hudson, Dakota(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Foul	
Pete Alonso grounds into a double play, third baseman Nolan Arenado to second baseman Tommy Edman to first baseman Albert Pujols. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-05-19	FF	92.8	2130	Hudson, Dakota(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Swinging Strike	
Pete Alonso grounds into a double play, third baseman Nolan Arenado to second baseman Tommy Edman to first baseman Albert Pujols. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-05-19	FF	95.1	2242	Pallante, Andre(R)	Alonso, Pete(R)	111.1	4°	122	
1-0	Bot 7	Hit Into Play	
Pete Alonso singles on a line drive to second baseman Tommy Edman, deflected by pitcher Andre Pallante. Francisco Lindor to 2nd.

2022-05-19	SL	85.9	2395	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso singles on a line drive to second baseman Tommy Edman, deflected by pitcher Andre Pallante. Francisco Lindor to 2nd.

2022-05-19	SI	93.2	1963	Hudson, Dakota(R)	Alonso, Pete(R)	78.0	8°	96	
0-1	Bot 1	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Dylan Carlson. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-05-19	SI	93.9	1991	Hudson, Dakota(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso singles on a ground ball to right fielder Dylan Carlson. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-05-19	SL	79.6	2338	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
3-0	Bot 5	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-19	SL	80.6	2332	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
2-0	Bot 5	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-19	SI	89.3	1909	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-19	SL	80.3	2302	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-19	FF	92.6	2395	Gallegos, Giovanny(R)	Alonso, Pete(R)	113.7	28°	447	
1-0	Bot 10	Hit Into Play	
Pete Alonso homers (10) on a fly ball to left field. Francisco Lindor scores.

2022-05-19	SL	84.7	2579	Gallegos, Giovanny(R)	Alonso, Pete(R)	--	°		
0-0	Bot 10	Ball	
Pete Alonso homers (10) on a fly ball to left field. Francisco Lindor scores.

2022-05-18	SI	98.8	2014	Hicks, Jordan(R)	Alonso, Pete(R)	74.1	57°	168	
1-0	Bot 3	Hit Into Play	
Pete Alonso pops out to shortstop Edmundo Sosa on the infield fly rule.

2022-05-18	SL	86.2	2517	Hicks, Jordan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso pops out to shortstop Edmundo Sosa on the infield fly rule.

2022-05-18	SI	101.0	2148	Hicks, Jordan(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Hit By Pitch	
Cardinals challenged (hit by pitch), call on the field was upheld: Pete Alonso hit by pitch. Mark Canha to 2nd.

2022-05-18	CH	82.4	1781	McFarland, T.J.(L)	Alonso, Pete(R)	107.8	18°	404	
1-1	Bot 8	Hit Into Play	
Pete Alonso homers (9) on a line drive to center field. Mark Canha scores. Francisco Lindor scores.

2022-05-18	SI	100.2	2233	Hicks, Jordan(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Cardinals challenged (hit by pitch), call on the field was upheld: Pete Alonso hit by pitch. Mark Canha to 2nd.

2022-05-18	ST	81.3	2401	VerHagen, Drew(R)	Alonso, Pete(R)	97.9	31°	348	
1-2	Bot 6	Hit Into Play	
Pete Alonso flies out to right fielder Juan Yepez.

2022-05-18	SI	88.3	1940	McFarland, T.J.(L)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso homers (9) on a line drive to center field. Mark Canha scores. Francisco Lindor scores.

2022-05-18	SI	100.5	2253	Hicks, Jordan(R)	Alonso, Pete(R)	63.7	53°	154	
0-0	Bot 1	Foul	
Cardinals challenged (hit by pitch), call on the field was upheld: Pete Alonso hit by pitch. Mark Canha to 2nd.

2022-05-18	FF	92.6	2354	VerHagen, Drew(R)	Alonso, Pete(R)	110.3	19°	322	
1-1	Bot 6	Foul	
Pete Alonso flies out to right fielder Juan Yepez.

2022-05-18	SL	78.9	2249	McFarland, T.J.(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso homers (9) on a line drive to center field. Mark Canha scores. Francisco Lindor scores.

2022-05-18	FF	94.5	2447	VerHagen, Drew(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Called Strike	
Pete Alonso flies out to right fielder Juan Yepez.

2022-05-18	ST	80.5	2344	VerHagen, Drew(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso flies out to right fielder Juan Yepez.

2022-05-18	SI	94.7	2384	Walsh, Jake(R)	Alonso, Pete(R)	99.4	-5°	18	
1-0	Bot 5	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Corey Dickerson. Mark Canha scores. Francisco Lindor to 2nd.

2022-05-18	SI	97.9	2524	Walsh, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a ground ball to left fielder Corey Dickerson. Mark Canha scores. Francisco Lindor to 2nd.

2022-05-17	SI	91.6	2252	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-17	SI	92.6	2329	Mikolas, Miles(R)	Alonso, Pete(R)	54.9	79°	66	
0-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-05-17	SL	85.8	2529	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Called Strike	
Pete Alonso strikes out swinging.

2022-05-17	CU	74.7	2504	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso strikes out swinging.

2022-05-17	SI	95.3	2344	Matz, Steven(L)	Alonso, Pete(R)	--	°		
2-2	Bot 4	Called Strike	
Pete Alonso called out on strikes.

2022-05-17	CH	84.7	2312	Matz, Steven(L)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Ball	
Pete Alonso called out on strikes.

2022-05-17	CU	77.9	2379	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Ball	
Pete Alonso called out on strikes.

2022-05-17	CU	75.9	2385	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Foul	
Pete Alonso called out on strikes.

2022-05-17	CU	76.3	2075	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso called out on strikes.

2022-05-17	SL	85.2	2391	Mikolas, Miles(R)	Alonso, Pete(R)	104.9	24°	389	
2-2	Bot 3	Hit Into Play	
Pete Alonso flies out sharply to center fielder Harrison Bader. Jeff McNeil to 3rd.

2022-05-17	SL	85.9	2488	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso flies out sharply to center fielder Harrison Bader. Jeff McNeil to 3rd.

2022-05-17	FF	91.0	2271	Mikolas, Miles(R)	Alonso, Pete(R)	48.7	42°	124	
1-1	Bot 3	Foul	
Pete Alonso flies out sharply to center fielder Harrison Bader. Jeff McNeil to 3rd.

2022-05-17	SI	90.4	2237	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso flies out sharply to center fielder Harrison Bader. Jeff McNeil to 3rd.

2022-05-17	FF	91.9	2338	Mikolas, Miles(R)	Alonso, Pete(R)	70.1	23°	186	
0-0	Bot 3	Foul	
Pete Alonso flies out sharply to center fielder Harrison Bader. Jeff McNeil to 3rd.

2022-05-17	SL	86.8	2429	Mikolas, Miles(R)	Alonso, Pete(R)	93.1	25°	349	
3-1	Bot 1	Hit Into Play	
Pete Alonso flies out to center fielder Harrison Bader.

2022-05-17	SL	85.6	2441	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso flies out to center fielder Harrison Bader.

2022-05-17	SL	86.5	2477	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso flies out to center fielder Harrison Bader.

2022-05-17	FF	91.6	2338	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso flies out to center fielder Harrison Bader.

2022-05-17	CH	84.7	2175	Matz, Steven(L)	Alonso, Pete(R)	85.7	44°	269	
1-0	Bot 1	Hit Into Play	
Pete Alonso flies out to right fielder Dylan Carlson.

2022-05-17	SL	85.7	2482	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Foul	
Pete Alonso flies out to center fielder Harrison Bader.

2022-05-17	FF	90.5	2110	Naughton, Packy(L)	Alonso, Pete(R)	65.3	18°	153	
2-0	Bot 8	Hit Into Play	
Pete Alonso lines out to shortstop Brendan Donovan.

2022-05-17	FF	90.9	2034	Naughton, Packy(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso lines out to shortstop Brendan Donovan.

2022-05-17	SI	95.0	2239	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out to right fielder Dylan Carlson.

2022-05-17	CU	76.5	2947	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
3-0	Bot 6	Blocked Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-17	FF	100.3	2622	Helsley, Ryan(R)	Alonso, Pete(R)	95.1	21°	327	
3-2	Bot 8	Hit Into Play	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	CH	80.7	1452	Naughton, Packy(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso lines out to shortstop Brendan Donovan.

2022-05-17	FF	98.2	2646	Helsley, Ryan(R)	Alonso, Pete(R)	98.4	64°	190	
3-2	Bot 8	Foul	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	FF	96.0	2467	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
2-0	Bot 6	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-17	FF	98.2	2596	Helsley, Ryan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Blocked Ball	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	FF	96.2	2448	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-17	SL	83.3	2394	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso walks. Mark Canha to 3rd. Francisco Lindor to 2nd.

2022-05-17	FF	98.1	2583	Helsley, Ryan(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Swinging Strike	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	SL	87.0	2401	Helsley, Ryan(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	FF	97.3	2511	Helsley, Ryan(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Swinging Strike	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-17	SL	85.3	2363	Helsley, Ryan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Blocked Ball	
Pete Alonso lines out to left fielder Tyler O'Neill.

2022-05-15	SL	87.5	2222	Ray, Robbie(L)	Alonso, Pete(R)	111.7	-4°	20	
3-2	Bot 5	Hit Into Play	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	SL	87.7	2015	Ray, Robbie(L)	Alonso, Pete(R)	77.6	-31°	4	
3-2	Bot 5	Foul	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	SL	87.6	2106	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Ball	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	SL	87.0	2294	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
2-1	Bot 5	Foul Tip	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	FF	94.3	2277	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	SL	88.0	2239	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Swinging Strike	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	FF	94.4	2419	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso grounds out, third baseman Abraham Toro to first baseman Ty France.

2022-05-15	KC	77.7	2156	Ray, Robbie(L)	Alonso, Pete(R)	104.0	9°	156	
0-0	Bot 4	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Jesse Winker.

2022-05-15	FF	95.3	2416	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-15	SL	89.3	2320	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
3-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-05-15	SL	88.4	2251	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-05-15	FF	95.1	2413	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	87.9	2189	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-15	SL	87.2	2175	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
3-2	Bot 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-15	FF	93.7	2518	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
3-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-15	FF	95.2	2383	Ray, Robbie(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	89.2	2270	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
2-2	Bot 9	Blocked Ball	
Pete Alonso strikes out swinging.

2022-05-15	FF	92.7	2496	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	87.4	2196	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
2-1	Bot 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-15	ST	83.4	2475	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-05-15	ST	84.0	2487	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	88.7	2269	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
1-1	Bot 9	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	87.4	2149	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
1-0	Bot 9	Called Strike	
Pete Alonso strikes out swinging.

2022-05-15	FF	93.5	2521	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-15	SL	88.5	1946	Castillo, Diego(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Blocked Ball	
Pete Alonso strikes out swinging.

2022-05-15	ST	81.8	2392	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-05-14	CU	78.7	2235	Kirby, George(R)	Alonso, Pete(R)	--	°		
3-1	Bot 3	Ball	
Pete Alonso walks.

2022-05-14	FF	96.1	2244	Kirby, George(R)	Alonso, Pete(R)	--	°		
2-1	Bot 3	Ball	
Pete Alonso walks.

2022-05-14	FC	89.2	2118	Kirby, George(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso walks.

2022-05-14	FF	96.0	2227	Kirby, George(R)	Alonso, Pete(R)	71.1	32°	218	
1-0	Bot 3	Foul	
Pete Alonso walks.

2022-05-14	CH	86.5	1518	Kirby, George(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso walks.

2022-05-14	FF	95.9	2120	Kirby, George(R)	Alonso, Pete(R)	99.5	35°	335	
3-1	Bot 1	Hit Into Play	
Pete Alonso flies out to right fielder Steven Souza Jr. Francisco Lindor to 3rd.

2022-05-14	FF	96.1	2297	Kirby, George(R)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso flies out to right fielder Steven Souza Jr. Francisco Lindor to 3rd.

2022-05-14	FC	89.5	2233	Kirby, George(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso flies out to right fielder Steven Souza Jr. Francisco Lindor to 3rd.

2022-05-14	FC	89.3	2185	Kirby, George(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso flies out to right fielder Steven Souza Jr. Francisco Lindor to 3rd.

2022-05-14	SL	86.7	2176	Muñoz, Andrés(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-14	FF	96.4	2366	Kirby, George(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Swinging Strike	
Pete Alonso flies out to right fielder Steven Souza Jr. Francisco Lindor to 3rd.

2022-05-14	SL	87.6	2279	Muñoz, Andrés(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-14	SL	83.3	2068	Muñoz, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso strikes out swinging.

2022-05-14	ST	79.6	2612	Murfee, Penn(R)	Alonso, Pete(R)	112.2	14°	314	
1-2	Bot 5	Hit Into Play	
Pete Alonso doubles (6) on a sharp line drive to left fielder Jesse Winker. Starling Marte scores.

2022-05-14	FF	88.9	2271	Murfee, Penn(R)	Alonso, Pete(R)	--	°		
0-2	Bot 5	Ball	
Pete Alonso doubles (6) on a sharp line drive to left fielder Jesse Winker. Starling Marte scores.

2022-05-14	FF	89.5	2299	Murfee, Penn(R)	Alonso, Pete(R)	75.0	17°	166	
0-2	Bot 5	Foul	
Pete Alonso doubles (6) on a sharp line drive to left fielder Jesse Winker. Starling Marte scores.

2022-05-14	FF	88.3	2190	Murfee, Penn(R)	Alonso, Pete(R)	72.4	27°	208	
0-1	Bot 5	Foul	
Pete Alonso doubles (6) on a sharp line drive to left fielder Jesse Winker. Starling Marte scores.

2022-05-14	ST	78.9	2647	Murfee, Penn(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso doubles (6) on a sharp line drive to left fielder Jesse Winker. Starling Marte scores.

2022-05-13	CH	80.2	2093	Gonzales, Marco(L)	Alonso, Pete(R)	109.9	-3°	37	
3-2	Bot 6	Hit Into Play	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	FF	88.9	2115	Gonzales, Marco(L)	Alonso, Pete(R)	75.8	68°	161	
3-1	Bot 6	Foul	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	FC	85.8	2158	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
2-1	Bot 6	Ball	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	FF	88.3	1971	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
2-0	Bot 6	Swinging Strike	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	FF	87.7	2069	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Ball	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	FC	86.9	1990	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso grounds out sharply, second baseman Adam Frazier to first baseman Ty France.

2022-05-13	CH	80.1	2218	Gonzales, Marco(L)	Alonso, Pete(R)	91.8	38°	307	
0-0	Bot 3	Hit Into Play	
Pete Alonso flies out to center fielder Julio Rodriguez.

2022-05-13	CH	80.8	2020	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-13	FF	91.2	2507	Sewald, Paul(R)	Alonso, Pete(R)	103.4	32°	381	
3-2	Bot 8	Hit Into Play	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-13	FF	89.6	1951	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-13	ST	83.5	2418	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Ball	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-13	CH	78.7	2164	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Blocked Ball	
Pete Alonso walks.

2022-05-13	FF	90.7	2569	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
1-2	Bot 8	Ball	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-13	FC	83.8	1986	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Ball	
Pete Alonso walks.

2022-05-13	ST	82.6	2518	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
0-2	Bot 8	Ball	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-13	FF	89.1	1890	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Foul Tip	
Pete Alonso walks.

2022-05-13	CH	79.6	2055	Gonzales, Marco(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso walks.

2022-05-13	FF	91.4	2519	Sewald, Paul(R)	Alonso, Pete(R)	78.4	21°	216	
0-1	Bot 8	Foul	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-13	FF	91.4	2528	Sewald, Paul(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Foul	
Pete Alonso flies out sharply to center fielder Julio Rodriguez.

2022-05-12	FF	93.8	2135	Adon, Joan(R)	Alonso, Pete(R)	92.7	0°	47	
2-2	Top 3	Hit Into Play	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	CU	80.9	2258	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-2	Top 3	Ball	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	FF	92.7	2223	Adon, Joan(R)	Alonso, Pete(R)	62.0	37°	173	
1-1	Top 3	Foul	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	FF	94.0	2313	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-0	Top 3	Called Strike	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	FF	92.4	2253	Adon, Joan(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	FF	94.3	2175	Adon, Joan(R)	Alonso, Pete(R)	--	°		
3-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-12	CU	81.7	2371	Adon, Joan(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-05-12	FF	94.5	2154	Adon, Joan(R)	Alonso, Pete(R)	--	°		
2-1	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-12	CU	79.2	2256	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-05-12	CU	78.6	2152	Adon, Joan(R)	Alonso, Pete(R)	87.1	-41°	2	
1-0	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-05-12	CU	79.7	2125	Adon, Joan(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-05-12	SI	93.7	2047	Ramírez, Erasmo(R)	Alonso, Pete(R)	67.8	-23°	7	
2-2	Top 5	Hit Into Play	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	FC	89.2	2347	Ramírez, Erasmo(R)	Alonso, Pete(R)	71.8	53°	196	
2-2	Top 5	Foul	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	SI	92.4	2105	Ramírez, Erasmo(R)	Alonso, Pete(R)	60.2	64°	122	
2-1	Top 5	Foul	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	FC	88.0	2334	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
1-1	Top 5	Ball	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	SI	93.0	2129	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	FC	89.3	2388	Ramírez, Erasmo(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Swinging Strike	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-05-12	SI	97.2	2191	Finnegan, Kyle(R)	Alonso, Pete(R)	72.3	7°	81	
2-2	Top 8	Hit Into Play	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	SL	89.2	2190	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
2-1	Top 8	Swinging Strike	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	SL	90.2	2218	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Ball	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	SI	98.1	2097	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-12	SL	88.1	2149	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-11	CU	78.4	2416	Sanchez, Aaron(R)	Alonso, Pete(R)	113.2	3°	102	
0-0	Top 6	Hit Into Play	
Pete Alonso singles on a sharp line drive to third baseman Maikel Franco, deflected by pitcher Aaron Sanchez.

2022-05-11	CU	79.0	2569	Sanchez, Aaron(R)	Alonso, Pete(R)	90.9	-2°	23	
0-2	Top 3	Hit Into Play	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-11	CU	78.6	2687	Sanchez, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 3	Swinging Strike	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-11	FF	91.6	2240	Sanchez, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso grounds out, shortstop Dee Strange-Gordon to first baseman Josh Bell.

2022-05-11	SL	86.2	2533	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
1-2	Top 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-11	SI	91.9	2047	Sanchez, Aaron(R)	Alonso, Pete(R)	101.7	31°	394	
1-0	Top 1	Hit Into Play	
Pete Alonso homers (8) on a fly ball to left field. Starling Marte scores.

2022-05-11	SL	85.9	2499	Arano, Víctor(R)	Alonso, Pete(R)	62.3	-8°	9	
1-2	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-05-11	SI	91.8	1941	Sanchez, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Blocked Ball	
Pete Alonso homers (8) on a fly ball to left field. Starling Marte scores.

2022-05-11	SL	85.3	2491	Arano, Víctor(R)	Alonso, Pete(R)	59.6	-56°	1	
1-1	Top 8	Foul	
Pete Alonso strikes out swinging.

2022-05-11	SL	83.6	2404	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Called Strike	
Pete Alonso strikes out swinging.

2022-05-11	SI	94.1	2126	Arano, Víctor(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso strikes out swinging.

2022-05-10	FF	90.0	2080	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
3-1	Top 4	Ball	
Pete Alonso walks.

2022-05-10	SL	81.2	2089	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-1	Top 4	Blocked Ball	
Pete Alonso walks.

2022-05-10	SL	81.1	2127	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-1	Top 4	Blocked Ball	
Pete Alonso walks.

2022-05-10	SL	80.6	2145	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Top 4	Called Strike	
Pete Alonso walks.

2022-05-10	SI	90.2	1942	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso walks.

2022-05-10	SI	90.4	2115	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
3-0	Top 2	Ball	
Pete Alonso walks.

2022-05-10	FF	91.8	2266	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-0	Top 2	Ball	
Pete Alonso walks.

2022-05-10	FF	90.8	2108	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso walks.

2022-05-10	SI	89.9	2085	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso walks.

2022-05-10	SL	75.6	2211	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
0-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-10	SL	77.0	2163	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-05-10	SL	76.8	2177	Cishek, Steve(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-05-10	FF	95.1	2573	Edwards Jr., Carl(R)	Alonso, Pete(R)	98.8	13°	210	
1-2	Top 6	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-05-10	CU	80.9	2217	Edwards Jr., Carl(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Ball	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-05-10	FF	95.7	2518	Edwards Jr., Carl(R)	Alonso, Pete(R)	97.8	39°	338	
0-1	Top 6	Foul	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-05-10	FF	94.8	2493	Edwards Jr., Carl(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Called Strike	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-05-08	SL	82.3	2449	Gibson, Kyle(R)	Alonso, Pete(R)	103.8	28°	359	
0-2	Top 5	Hit Into Play	
Pete Alonso flies out sharply to center fielder Odubel Herrera.

2022-05-08	CH	83.5	1619	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Swinging Strike	
Pete Alonso flies out sharply to center fielder Odubel Herrera.

2022-05-08	SI	90.6	2077	Gibson, Kyle(R)	Alonso, Pete(R)	112.6	32°	405	
0-0	Top 5	Foul	
Pete Alonso flies out sharply to center fielder Odubel Herrera.

2022-05-08	FF	94.2	1847	Nelson, Nick(R)	Alonso, Pete(R)	111.4	29°	426	
2-0	Top 5	Hit Into Play	
Pete Alonso homers (7) on a fly ball to left field. Brandon Nimmo scores. Mark Canha scores.

2022-05-08	FF	95.2	1748	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Ball	
Pete Alonso homers (7) on a fly ball to left field. Brandon Nimmo scores. Mark Canha scores.

2022-05-08	FF	96.5	1699	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso homers (7) on a fly ball to left field. Brandon Nimmo scores. Mark Canha scores.

2022-05-08	SI	91.8	2100	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
3-2	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-05-08	SI	91.3	2161	Gibson, Kyle(R)	Alonso, Pete(R)	85.0	-17°	7	
3-2	Top 2	Foul	
Pete Alonso called out on strikes.

2022-05-08	FC	87.2	2258	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Ball	
Pete Alonso called out on strikes.

2022-05-08	SI	91.6	2286	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
2-1	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-05-08	SL	82.8	2401	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Ball	
Pete Alonso called out on strikes.

2022-05-08	SI	90.5	2094	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-05-08	SL	83.8	2503	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso called out on strikes.

2022-05-08	CH	84.1	2018	Sánchez, Cristopher(L)	Alonso, Pete(R)	103.5	27°	382	
2-2	Top 1	Hit Into Play	
Pete Alonso homers (6) on a fly ball to left field. Francisco Lindor scores.

2022-05-08	SI	94.0	2094	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso homers (6) on a fly ball to left field. Francisco Lindor scores.

2022-05-08	SI	93.3	2143	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
1-1	Top 1	Swinging Strike	
Pete Alonso homers (6) on a fly ball to left field. Francisco Lindor scores.

2022-05-08	SI	92.8	2177	Sánchez, Cristopher(L)	Alonso, Pete(R)	75.6	6°	86	
1-0	Top 1	Foul	
Pete Alonso homers (6) on a fly ball to left field. Francisco Lindor scores.

2022-05-08	SI	92.9	2147	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso homers (6) on a fly ball to left field. Francisco Lindor scores.

2022-05-08	CH	82.2	1910	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
3-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-08	SL	91.6	1961	Norwood, James(R)	Alonso, Pete(R)	96.8	24°	360	
1-1	Top 9	Hit Into Play	
Pete Alonso flies out to center fielder Roman Quinn.

2022-05-08	CH	83.5	1959	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
2-2	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-05-08	SL	91.5	1975	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-1	Top 9	Ball	
Pete Alonso flies out to center fielder Roman Quinn.

2022-05-08	FC	89.2	2392	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
2-1	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-08	FF	97.9	2092	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso flies out to center fielder Roman Quinn.

2022-05-08	FF	93.1	2230	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
2-0	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-05-08	FF	96.9	2337	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-08	FF	94.9	2247	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
1-0	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-05-08	FF	95.8	2396	Knebel, Corey(R)	Alonso, Pete(R)	77.0	12°	142	
2-2	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-05-08	KC	77.0	2886	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-05-08	FC	89.0	2321	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-05-08	FF	96.8	2330	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
3-0	Top 7	Ball	
Pete Alonso walks.

2022-05-08	FF	96.8	1849	Nelson, Nick(R)	Alonso, Pete(R)	104.5	13°	265	
0-0	Top 3	Hit Into Play	
Pete Alonso singles on a sharp line drive to center fielder Roman Quinn. Brandon Nimmo to 3rd.

2022-05-08	SI	97.8	2249	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
2-0	Top 7	Ball	
Pete Alonso walks.

2022-05-08	FF	97.1	2236	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
1-1	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-05-08	SI	97.3	2254	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
1-0	Top 7	Ball	
Pete Alonso walks.

2022-05-08	FF	96.7	2208	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Foul Tip	
Pete Alonso strikes out swinging.

2022-05-08	FF	96.7	2237	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-05-08	SI	97.5	2256	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso walks.

2022-05-05	KC	78.7	2479	Nola, Aaron(R)	Alonso, Pete(R)	55.6	-40°	2	
1-2	Top 7	Hit Into Play	
Pete Alonso grounds out softly to first baseman Rhys Hoskins.

2022-05-05	SI	90.4	2019	Nola, Aaron(R)	Alonso, Pete(R)	74.3	18°	176	
1-1	Top 7	Foul	
Pete Alonso grounds out softly to first baseman Rhys Hoskins.

2022-05-05	KC	78.2	2674	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Ball	
Pete Alonso grounds out softly to first baseman Rhys Hoskins.

2022-05-05	SI	89.3	2202	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso grounds out softly to first baseman Rhys Hoskins.

2022-05-05	SI	90.3	2172	Nola, Aaron(R)	Alonso, Pete(R)	73.6	14°	160	
0-1	Top 4	Hit Into Play	
Pete Alonso lines out to shortstop Johan Camargo.

2022-05-05	FC	87.3	2101	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso lines out to shortstop Johan Camargo.

2022-05-05	FF	92.3	2163	Nola, Aaron(R)	Alonso, Pete(R)	104.6	5°	120	
1-1	Top 2	Hit Into Play	
Pete Alonso singles on a sharp ground ball to center fielder Odubel Herrera.

2022-05-05	FF	92.2	2221	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Pete Alonso singles on a sharp ground ball to center fielder Odubel Herrera.

2022-05-05	SI	90.9	2096	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso singles on a sharp ground ball to center fielder Odubel Herrera.

2022-05-05	FF	96.5	2227	Norwood, James(R)	Alonso, Pete(R)	84.2	12°	161	
0-1	Top 9	Hit Into Play	
Pete Alonso doubles (5) on a line drive to left fielder Kyle Schwarber.

2022-05-05	FS	88.5	1616	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Swinging Strike	
Pete Alonso doubles (5) on a line drive to left fielder Kyle Schwarber.

2022-05-04	CH	87.0	1556	Anderson, Ian(R)	Alonso, Pete(R)	95.2	21°	299	
0-0	Bot 6	Hit Into Play	
Pete Alonso doubles (4) on a line drive to left fielder Marcell Ozuna.

2022-05-04	CH	87.8	1581	Anderson, Ian(R)	Alonso, Pete(R)	88.5	5°	85	
1-2	Bot 3	Hit Into Play	
Pete Alonso grounds into a force out, shortstop Dansby Swanson to second baseman Ozzie Albies. Starling Marte out at 2nd.

2022-05-04	FF	92.8	1829	Anderson, Ian(R)	Alonso, Pete(R)	73.9	37°	200	
1-2	Bot 3	Foul	
Pete Alonso grounds into a force out, shortstop Dansby Swanson to second baseman Ozzie Albies. Starling Marte out at 2nd.

2022-05-04	FF	91.4	1880	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Foul Tip	
Pete Alonso grounds into a force out, shortstop Dansby Swanson to second baseman Ozzie Albies. Starling Marte out at 2nd.

2022-05-04	FF	92.2	1821	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso grounds into a force out, shortstop Dansby Swanson to second baseman Ozzie Albies. Starling Marte out at 2nd.

2022-05-04	FF	92.6	1947	Anderson, Ian(R)	Alonso, Pete(R)	73.1	43°	203	
0-0	Bot 3	Foul	
Pete Alonso grounds into a force out, shortstop Dansby Swanson to second baseman Ozzie Albies. Starling Marte out at 2nd.

2022-05-04	FF	92.8	1827	Anderson, Ian(R)	Alonso, Pete(R)	93.6	40°	313	
3-2	Bot 1	Hit Into Play	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	CH	87.5	1574	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	FF	92.8	1809	Anderson, Ian(R)	Alonso, Pete(R)	98.9	8°	128	
2-1	Bot 1	Foul	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	FF	92.4	1856	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	CU	81.2	1938	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Swinging Strike	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	CU	81.1	2010	Anderson, Ian(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out to left fielder Marcell Ozuna.

2022-05-04	FF	96.7	2382	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-04	FF	96.7	2425	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-04	CH	87.3	1826	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-04	CH	87.4	1834	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-04	FF	96.2	2319	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-05-03	FF	93.6	2249	Morton, Charlie(R)	Alonso, Pete(R)	95.7	31°	315	
1-2	Bot 5	Hit Into Play	
Pete Alonso flies out to right fielder Travis Demeritte.

2022-05-03	CU	81.0	2984	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Called Strike	
Pete Alonso flies out to right fielder Travis Demeritte.

2022-05-03	CU	80.2	2865	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Called Strike	
Pete Alonso flies out to right fielder Travis Demeritte.

2022-05-03	SI	93.4	2083	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso flies out to right fielder Travis Demeritte.

2022-05-03	SI	94.1	2228	Wright, Kyle(R)	Alonso, Pete(R)	107.0	26°	378	
2-2	Bot 6	Hit Into Play	
Pete Alonso homers (5) on a fly ball to right center field.

2022-05-03	KC	84.7	2759	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso homers (5) on a fly ball to right center field.

2022-05-03	FF	94.2	2268	Wright, Kyle(R)	Alonso, Pete(R)	94.4	54°	202	
1-1	Bot 6	Foul	
Pete Alonso homers (5) on a fly ball to right center field.

2022-05-03	SI	93.9	2216	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Called Strike	
Pete Alonso homers (5) on a fly ball to right center field.

2022-05-03	SI	93.2	2115	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso homers (5) on a fly ball to right center field.

2022-05-03	CU	82.6	2966	Morton, Charlie(R)	Alonso, Pete(R)	110.2	3°	99	
2-1	Bot 2	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Guillermo Heredia. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	SI	95.3	2243	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-0	Bot 2	Called Strike	
Pete Alonso singles on a ground ball to left fielder Guillermo Heredia. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	SI	94.1	2239	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-0	Bot 2	Ball	
Pete Alonso singles on a ground ball to left fielder Guillermo Heredia. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	FC	87.6	2664	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso singles on a ground ball to left fielder Guillermo Heredia. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	KC	85.2	2904	Wright, Kyle(R)	Alonso, Pete(R)	66.3	21°	166	
2-2	Bot 3	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Jeff McNeil to 3rd.

2022-05-03	SI	93.4	2220	Wright, Kyle(R)	Alonso, Pete(R)	99.8	-28°	4	
2-1	Bot 3	Foul	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Jeff McNeil to 3rd.

2022-05-03	KC	83.1	2787	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Ball	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Jeff McNeil to 3rd.

2022-05-03	CH	86.5	1715	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Jeff McNeil to 3rd.

2022-05-03	FF	94.8	2418	Wright, Kyle(R)	Alonso, Pete(R)	77.4	26°	229	
0-0	Bot 3	Foul	
Pete Alonso singles on a line drive to right fielder Ronald Acuna Jr. Jeff McNeil to 3rd.

2022-05-03	FF	96.6	2466	Morton, Charlie(R)	Alonso, Pete(R)	73.9	12°	135	
3-2	Bot 1	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	FF	95.8	2457	Morton, Charlie(R)	Alonso, Pete(R)	63.0	45°	161	
3-1	Bot 1	Foul	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	FF	94.7	2399	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
3-0	Bot 1	Called Strike	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	SI	96.3	2315	Wright, Kyle(R)	Alonso, Pete(R)	74.6	-27°	2	
1-2	Bot 1	Hit Into Play	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-05-03	SI	95.5	2344	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	FF	96.2	2401	Wright, Kyle(R)	Alonso, Pete(R)	80.3	35°	232	
1-2	Bot 1	Foul	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-05-03	CH	87.8	1661	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Foul	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-05-03	CU	81.8	3086	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	CU	81.4	2966	Morton, Charlie(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso singles on a ground ball to right fielder Travis Demeritte. Travis Jankowski scores. Francisco Lindor to 2nd.

2022-05-03	SL	91.1	2538	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-05-03	FC	88.9	2156	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Called Strike	
Pete Alonso called out on strikes.

2022-05-03	SI	95.5	2345	Wright, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso grounds out, shortstop Dansby Swanson to first baseman Matt Olson. Brandon Nimmo to 3rd. Jeff McNeil to 2nd.

2022-05-03	FC	89.0	2059	Chavez, Jesse(R)	Alonso, Pete(R)	72.5	11°	117	
0-2	Bot 7	Foul	
Pete Alonso called out on strikes.

2022-05-03	FC	89.0	2211	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Swinging Strike	
Pete Alonso called out on strikes.

2022-05-03	SI	90.7	1876	Chavez, Jesse(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso called out on strikes.

2022-05-03	SL	80.5	2357	Smith, Will(L)	Alonso, Pete(R)	84.2	42°	260	
2-2	Bot 8	Hit Into Play	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-03	SL	79.7	2247	Smith, Will(L)	Alonso, Pete(R)	--	°		
1-2	Bot 8	Ball	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-03	FF	91.2	2225	Smith, Will(L)	Alonso, Pete(R)	71.2	51°	194	
1-2	Bot 8	Foul	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-03	CU	75.9	1824	Smith, Will(L)	Alonso, Pete(R)	77.2	3°	59	
1-1	Bot 8	Foul	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-03	CU	74.1	1747	Smith, Will(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Called Strike	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-03	FF	90.1	2045	Smith, Will(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso flies out to left fielder Travis Demeritte.

2022-05-02	CH	87.6	1605	Fried, Max(L)	Alonso, Pete(R)	80.8	-13°	13	
1-2	Bot 6	Hit Into Play	
Pete Alonso grounds out, second baseman Ozzie Albies to first baseman Matt Olson.

2022-05-02	CH	88.7	1495	Fried, Max(L)	Alonso, Pete(R)	66.3	-42°	3	
1-1	Bot 6	Foul	
Pete Alonso grounds out, second baseman Ozzie Albies to first baseman Matt Olson.

2022-05-02	CU	75.2	2786	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Bot 6	Ball	
Pete Alonso grounds out, second baseman Ozzie Albies to first baseman Matt Olson.

2022-05-02	FF	94.2	2154	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Called Strike	
Pete Alonso grounds out, second baseman Ozzie Albies to first baseman Matt Olson.

2022-05-02	FF	92.8	2017	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Called Strike	
Pete Alonso called out on strikes.

2022-05-02	CH	86.8	1538	Fried, Max(L)	Alonso, Pete(R)	--	°		
1-1	Bot 3	Swinging Strike	
Pete Alonso called out on strikes.

2022-05-02	SL	85.8	2289	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Ball	
Pete Alonso called out on strikes.

2022-05-02	SL	84.9	2376	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Swinging Strike	
Pete Alonso called out on strikes.

2022-05-02	FF	94.0	2257	Fried, Max(L)	Alonso, Pete(R)	60.0	41°	176	
0-1	Bot 1	Hit Into Play	
Pete Alonso pops out to shortstop Dansby Swanson on the infield fly rule.

2022-05-02	CU	74.5	2620	Fried, Max(L)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso pops out to shortstop Dansby Swanson on the infield fly rule.

2022-05-02	FF	96.5	2375	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-02	FF	96.2	2355	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-05-02	CH	85.9	1698	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-05-02	FF	96.7	2306	Minter, A.J.(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-05-01	SI	91.2	2042	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Zach Eflin intentionally walks Pete Alonso.

2022-05-01	FC	91.5	2201	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Blocked Ball	
Zach Eflin intentionally walks Pete Alonso.

2022-05-01	SI	92.4	2038	Eflin, Zach(R)	Alonso, Pete(R)	83.0	-3°	25	
1-0	Bot 3	Hit Into Play	
Pete Alonso grounds out, shortstop Johan Camargo to first baseman Rhys Hoskins.

2022-05-01	SI	92.6	1961	Eflin, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso grounds out, shortstop Johan Camargo to first baseman Rhys Hoskins.

2022-05-01	SL	85.7	1812	Sánchez, Cristopher(L)	Alonso, Pete(R)	72.4	-22°	2	
2-2	Bot 8	Hit Into Play	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-01	SI	93.1	1892	Sánchez, Cristopher(L)	Alonso, Pete(R)	71.4	28°	157	
2-1	Bot 8	Foul	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-01	SI	93.8	1933	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
2-0	Bot 8	Called Strike	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-01	SI	92.5	1892	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-01	SI	94.1	1932	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Blocked Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins.

2022-05-01	FS	90.4	1429	Norwood, James(R)	Alonso, Pete(R)	88.4	11°	194	
2-2	Bot 7	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	SI	92.7	2107	Eflin, Zach(R)	Alonso, Pete(R)	90.5	24°	314	
0-0	Bot 2	Hit Into Play	
Pete Alonso lines out to center fielder Odubel Herrera.

2022-05-01	FF	94.0	1823	Norwood, James(R)	Alonso, Pete(R)	--	°		
1-2	Bot 7	Ball	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	FF	95.8	1771	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Ball	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	FF	95.9	2107	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Foul	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	SI	96.5	2127	Norwood, James(R)	Alonso, Pete(R)	57.3	56°	132	
0-2	Bot 7	Foul	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	FF	96.2	2196	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Called Strike	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-05-01	FF	95.9	2211	Norwood, James(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Swinging Strike	
Pete Alonso singles on a line drive to right fielder Nick Castellanos. Francisco Lindor scores. Jeff McNeil to 2nd.

2022-04-30	SI	90.6	2185	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
3-1	Bot 5	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-04-30	SI	91.0	2044	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
2-1	Bot 5	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-04-30	SL	82.3	2425	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Blocked Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-04-30	SL	83.6	2460	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Swinging Strike	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-04-30	SI	90.5	2191	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso walks. Starling Marte to 3rd. Francisco Lindor to 2nd.

2022-04-30	SL	82.4	2461	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-30	SI	89.0	2092	Gibson, Kyle(R)	Alonso, Pete(R)	106.8	-1°	41	
0-1	Bot 4	Foul	
Pete Alonso strikes out swinging.

2022-04-30	SI	89.7	2109	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso strikes out swinging.

2022-04-30	FF	94.7	2371	Knebel, Corey(R)	Alonso, Pete(R)	90.9	49°	239	
3-2	Bot 9	Hit Into Play	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	FF	95.5	2455	Knebel, Corey(R)	Alonso, Pete(R)	80.3	13°	150	
3-2	Bot 9	Foul	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	FF	94.8	2352	Knebel, Corey(R)	Alonso, Pete(R)	74.5	43°	204	
3-1	Bot 9	Foul	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	KC	78.1	2955	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
2-1	Bot 9	Blocked Ball	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	FF	95.5	2395	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
1-1	Bot 9	Ball	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	FF	96.4	2412	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
0-1	Bot 9	Ball	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	FF	93.7	2369	Knebel, Corey(R)	Alonso, Pete(R)	--	°		
0-0	Bot 9	Called Strike	
Pete Alonso flies out to right fielder Nick Castellanos.

2022-04-30	SI	92.4	2127	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	91.9	2125	Gibson, Kyle(R)	Alonso, Pete(R)	67.9	-47°	2	
3-2	Bot 1	Foul	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	92.6	2090	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
3-1	Bot 1	Called Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	92.5	2231	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
2-1	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SL	83.7	2466	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	91.5	1989	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Ball	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	92.4	2111	Gibson, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso walks. Francisco Lindor to 2nd.

2022-04-30	SI	95.0	2198	Familia, Jeurys(R)	Alonso, Pete(R)	91.2	10°	168	
3-1	Bot 7	Hit Into Play	
Pete Alonso lines out to second baseman Jean Segura.

2022-04-30	SI	94.1	2238	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
3-0	Bot 7	Called Strike	
Pete Alonso lines out to second baseman Jean Segura.

2022-04-30	SI	94.1	2118	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
2-0	Bot 7	Ball	
Pete Alonso lines out to second baseman Jean Segura.

2022-04-30	SI	94.9	2119	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso lines out to second baseman Jean Segura.

2022-04-30	SL	87.0	2095	Familia, Jeurys(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso lines out to second baseman Jean Segura.

2022-04-29	CH	83.6	1387	Nola, Aaron(R)	Alonso, Pete(R)	98.2	33°	382	
0-0	Bot 6	Hit Into Play	
Pete Alonso homers (4) on a fly ball to left field.

2022-04-29	KC	79.5	2545	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
3-2	Bot 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-29	SI	92.5	2247	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
2-2	Bot 4	Ball	
Pete Alonso strikes out swinging.

2022-04-29	FF	90.9	2245	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-2	Bot 4	Ball	
Pete Alonso strikes out swinging.

2022-04-29	KC	78.2	2579	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-1	Bot 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-29	KC	79.9	2704	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Ball	
Pete Alonso strikes out swinging.

2022-04-29	FF	90.3	2277	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso strikes out swinging.

2022-04-29	FF	97.1	2094	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
3-2	Bot 8	Called Strike	
Pete Alonso called out on strikes.

2022-04-29	CH	89.3	1881	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Ball	
Pete Alonso called out on strikes.

2022-04-29	CU	83.9	2446	Nelson, Nick(R)	Alonso, Pete(R)	69.1	61°	153	
2-1	Bot 8	Foul	
Pete Alonso called out on strikes.

2022-04-29	FF	96.9	2110	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso called out on strikes.

2022-04-29	FF	96.5	2039	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Called Strike	
Pete Alonso called out on strikes.

2022-04-29	FF	96.4	1893	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso called out on strikes.

2022-04-29	KC	79.0	2624	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
3-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-29	FF	89.8	2329	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
2-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-04-29	KC	79.4	2548	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-04-29	KC	79.2	2521	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Ball	
Pete Alonso strikes out swinging.

2022-04-29	FF	92.5	2399	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-04-29	FF	91.1	2274	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Called Strike	
Pete Alonso strikes out swinging.

2022-04-27	SI	92.1	2244	Matz, Steven(L)	Alonso, Pete(R)	--	°		
3-0	Top 3	Ball	
Pete Alonso walks.

2022-04-27	CH	83.9	2201	Matz, Steven(L)	Alonso, Pete(R)	--	°		
2-0	Top 3	Ball	
Pete Alonso walks.

2022-04-27	SI	93.2	2394	Matz, Steven(L)	Alonso, Pete(R)	--	°		
1-0	Top 3	Ball	
Pete Alonso walks.

2022-04-27	SI	92.6	2296	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Ball	
Pete Alonso walks.

2022-04-27	SI	94.6	2216	Matz, Steven(L)	Alonso, Pete(R)	100.5	7°	167	
1-2	Top 2	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Corey Dickerson.

2022-04-27	CH	82.8	2350	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-2	Top 2	Ball	
Pete Alonso singles on a line drive to right fielder Corey Dickerson.

2022-04-27	CH	84.4	2302	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-1	Top 2	Swinging Strike	
Pete Alonso singles on a line drive to right fielder Corey Dickerson.

2022-04-27	CU	75.7	2472	Matz, Steven(L)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso singles on a line drive to right fielder Corey Dickerson.

2022-04-27	CH	89.5	1870	Cabrera, Génesis(L)	Alonso, Pete(R)	62.9	-3°	22	
1-0	Top 7	Hit Into Play	
Pete Alonso grounds out to first baseman Paul Goldschmidt.

2022-04-27	CU	78.4		Cabrera, Génesis(L)	Alonso, Pete(R)	--	°		
0-0	Top 7	Blocked Ball	
Pete Alonso grounds out to first baseman Paul Goldschmidt.

2022-04-27	ST	82.3	2513	Woodford, Jake(R)	Alonso, Pete(R)	94.6	28°	361	
1-2	Top 5	Hit Into Play	
Pete Alonso flies out to left fielder Tyler O'Neill.

2022-04-27	FF	93.0	2379	Woodford, Jake(R)	Alonso, Pete(R)	102.7	7°	120	
1-1	Top 5	Foul	
Pete Alonso flies out to left fielder Tyler O'Neill.

2022-04-27	ST	83.3	2579	Woodford, Jake(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso flies out to left fielder Tyler O'Neill.

2022-04-27	ST	82.8	2387	Woodford, Jake(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso flies out to left fielder Tyler O'Neill.

2022-04-26	FF	93.4	2234	Pallante, Andre(R)	Alonso, Pete(R)	107.8	-18°	5	
0-2	Top 3	Hit Into Play	
Pete Alonso grounds out, second baseman Tommy Edman to first baseman Brendan Donovan.

2022-04-26	SI	95.8	2176	Hicks, Jordan(R)	Alonso, Pete(R)	106.5	-16°	9	
0-0	Top 2	Hit Into Play	
Pete Alonso grounds out, shortstop Paul DeJong to first baseman Brendan Donovan.

2022-04-26	CU	74.5	2782	Pallante, Andre(R)	Alonso, Pete(R)	69.7	-29°	2	
0-2	Top 3	Foul	
Pete Alonso grounds out, second baseman Tommy Edman to first baseman Brendan Donovan.

2022-04-26	FF	94.8	2280	Pallante, Andre(R)	Alonso, Pete(R)	76.9	30°	226	
0-2	Top 3	Foul	
Pete Alonso grounds out, second baseman Tommy Edman to first baseman Brendan Donovan.

2022-04-26	SL	83.0	2235	Pallante, Andre(R)	Alonso, Pete(R)	72.2	51°	195	
0-1	Top 3	Foul	
Pete Alonso grounds out, second baseman Tommy Edman to first baseman Brendan Donovan.

2022-04-26	CU	75.2	2809	Pallante, Andre(R)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Pete Alonso grounds out, second baseman Tommy Edman to first baseman Brendan Donovan.

2022-04-26	FC	86.5	2282	Wittgren, Nick(R)	Alonso, Pete(R)	71.5	-38°	2	
2-2	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	CH	83.1	1986	Whitley, Kodi(R)	Alonso, Pete(R)	--	°		
1-2	Top 8	Hit By Pitch	
Pete Alonso hit by pitch.

2022-04-26	FF	92.2	2164	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
1-2	Top 6	Ball	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	CH	85.7	1942	Wittgren, Nick(R)	Alonso, Pete(R)	99.4	1°	59	
1-2	Top 6	Foul	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	CH	82.9	1943	Whitley, Kodi(R)	Alonso, Pete(R)	--	°		
1-1	Top 8	Swinging Strike	
Pete Alonso hit by pitch.

2022-04-26	CH	83.7	2009	Whitley, Kodi(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Ball	
Pete Alonso hit by pitch.

2022-04-26	FF	92.5	2186	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Ball	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	FF	92.1	2168	Wittgren, Nick(R)	Alonso, Pete(R)	70.5	57°	168	
0-2	Top 6	Foul	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	FF	92.1	2188	Whitley, Kodi(R)	Alonso, Pete(R)	45.1	-33°	4	
0-0	Top 8	Foul	
Pete Alonso hit by pitch.

2022-04-26	CH	84.2	1900	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Foul	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-26	SI	90.9	2104	Wittgren, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Swinging Strike	
Pete Alonso grounds out, third baseman Nolan Arenado to first baseman Brendan Donovan.

2022-04-25	SI	94.3	2300	Mikolas, Miles(R)	Alonso, Pete(R)	93.1	5°	103	
1-0	Top 6	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Dylan Carlson.

2022-04-25	SI	94.0	2226	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso singles on a ground ball to right fielder Dylan Carlson.

2022-04-25	FF	94.4	2298	Mikolas, Miles(R)	Alonso, Pete(R)	94.0	18°	287	
0-2	Top 4	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Harrison Bader.

2022-04-25	SL	88.2	2461	Mikolas, Miles(R)	Alonso, Pete(R)	65.1	32°	154	
0-1	Top 4	Foul	
Pete Alonso singles on a line drive to center fielder Harrison Bader.

2022-04-25	FF	94.4	2349	Mikolas, Miles(R)	Alonso, Pete(R)	75.5	15°	167	
0-0	Top 4	Foul	
Pete Alonso singles on a line drive to center fielder Harrison Bader.

2022-04-25	SL	88.0	2469	Mikolas, Miles(R)	Alonso, Pete(R)	79.9	64°	143	
1-2	Top 2	Hit Into Play	
Pete Alonso pops out to first baseman Paul Goldschmidt in foul territory.

2022-04-25	CU	75.6	2519	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
1-1	Top 2	Called Strike	
Pete Alonso pops out to first baseman Paul Goldschmidt in foul territory.

2022-04-25	SL	87.0	2361	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Called Strike	
Pete Alonso pops out to first baseman Paul Goldschmidt in foul territory.

2022-04-25	SL	86.0	2447	Mikolas, Miles(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso pops out to first baseman Paul Goldschmidt in foul territory.

2022-04-25	FF	93.5	2399	Gallegos, Giovanny(R)	Alonso, Pete(R)	95.5	43°	307	
0-0	Top 9	Hit Into Play	
Pete Alonso flies out to center fielder Harrison Bader.

2022-04-24	CH	81.8	1316	Bumgarner, Madison(L)	Alonso, Pete(R)	79.2	-25°	3	
1-0	Top 4	Hit Into Play	
Pete Alonso grounds into a force out, third baseman Sergio Alcantara to second baseman Geraldo Perdomo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-24	CU	63.4	1708	Bumgarner, Madison(L)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso grounds into a force out, third baseman Sergio Alcantara to second baseman Geraldo Perdomo. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-24	CH	84.2	1378	Bumgarner, Madison(L)	Alonso, Pete(R)	--	°		
2-2	Top 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-24	FC	88.0	2257	Bumgarner, Madison(L)	Alonso, Pete(R)	97.1	-12°	16	
2-2	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-04-24	FF	91.0	2182	Bumgarner, Madison(L)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-04-24	SL	88.0	2477	Wendelken, J.B.(R)	Alonso, Pete(R)	85.5	10°	133	
1-1	Top 6	Hit Into Play	
Pete Alonso grounds out, second baseman Geraldo Perdomo to first baseman Christian Walker.

2022-04-24	CU	77.1	2270	Bumgarner, Madison(L)	Alonso, Pete(R)	87.8	20°	251	
1-2	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-04-24	CH	86.6	1671	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Swinging Strike	
Pete Alonso grounds out, second baseman Geraldo Perdomo to first baseman Christian Walker.

2022-04-24	FC	88.3	2183	Bumgarner, Madison(L)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-04-24	CH	84.3	1402	Bumgarner, Madison(L)	Alonso, Pete(R)	64.3	4°	54	
0-1	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-04-24	SI	94.4	2217	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out, second baseman Geraldo Perdomo to first baseman Christian Walker.

2022-04-24	CU	76.0	2189	Bumgarner, Madison(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-04-24	CH	83.5	1516	Widener, Taylor(R)	Alonso, Pete(R)	95.0	0°	50	
0-1	Top 8	Hit Into Play	
Pete Alonso grounds out, first baseman Christian Walker to pitcher Taylor Widener.

2022-04-24	FF	92.1	1847	Widener, Taylor(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso grounds out, first baseman Christian Walker to pitcher Taylor Widener.

2022-04-24	FF	94.5	2488	Martin, Corbin(R)	Alonso, Pete(R)	107.2	10°	182	
0-0	Top 9	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder David Peralta.

2022-04-23	SI	89.7	2059	Castellanos, Humberto(R)	Alonso, Pete(R)	95.4	52°	270	
0-0	Top 4	Hit Into Play	
Pete Alonso flies out to center fielder Daulton Varsho.

2022-04-23	SI	90.5	2125	Castellanos, Humberto(R)	Alonso, Pete(R)	81.7	50°	233	
1-2	Top 1	Hit Into Play	
Pete Alonso flies out to left fielder David Peralta.

2022-04-23	CU	76.9	2483	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
1-1	Top 1	Called Strike	
Pete Alonso flies out to left fielder David Peralta.

2022-04-23	CH	81.2	2194	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
3-2	Top 6	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-04-23	CH	81.2	2041	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
3-1	Top 6	Called Strike	
Pete Alonso strikes out swinging.

2022-04-23	CU	78.2	2585	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
0-1	Top 1	Blocked Ball	
Pete Alonso flies out to left fielder David Peralta.

2022-04-23	SI	90.4	2078	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Called Strike	
Pete Alonso flies out to left fielder David Peralta.

2022-04-23	CU	78.3	2586	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
2-1	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-04-23	CU	79.3	2550	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-04-23	CH	83.1	1938	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Ball	
Pete Alonso strikes out swinging.

2022-04-23	FF	95.0	2455	Kennedy, Ian(R)	Alonso, Pete(R)	--	°		
1-2	Top 8	Called Strike	
Pete Alonso called out on strikes.

2022-04-23	CH	83.0	1969	Ramirez, Noé(R)	Alonso, Pete(R)	61.6	-41°	2	
0-0	Top 6	Foul	
Pete Alonso strikes out swinging.

2022-04-23	FF	93.9	2479	Kennedy, Ian(R)	Alonso, Pete(R)	102.1	47°		
1-2	Top 8	Foul	
Pete Alonso called out on strikes.

2022-04-23	FF	94.2	2486	Kennedy, Ian(R)	Alonso, Pete(R)	--	°		
0-2	Top 8	Ball	
Pete Alonso called out on strikes.

2022-04-23	FF	94.4	2396	Kennedy, Ian(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Called Strike	
Pete Alonso called out on strikes.

2022-04-23	FF	94.6	2373	Kennedy, Ian(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso called out on strikes.

2022-04-22	CH	86.2	1520	Gallen, Zac(R)	Alonso, Pete(R)	79.5	57°	181	
2-2	Top 4	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	FF	93.9	2494	Gallen, Zac(R)	Alonso, Pete(R)	71.7	25°	202	
2-2	Top 4	Foul	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	CH	86.7	1391	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
2-1	Top 4	Swinging Strike Blocked	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	FF	93.8	2386	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	FF	93.3	2410	Gallen, Zac(R)	Alonso, Pete(R)	72.6	46°	239	
1-0	Top 4	Foul	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	KC	82.8	2515	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso singles on a fly ball to right fielder Pavin Smith. Brandon Nimmo scores. Francisco Lindor to 2nd.

2022-04-22	FF	93.9	2396	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-2	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-22	FF	92.9	2363	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-1	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-22	FF	93.5	2465	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-22	CH	89.8	2239	Uceta, Edwin(R)	Alonso, Pete(R)	86.2	49°	245	
0-2	Top 8	Hit Into Play	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-22	CH	90.0	2234	Uceta, Edwin(R)	Alonso, Pete(R)	--	°		
0-1	Top 8	Swinging Strike	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-22	CU	82.6	2600	Uceta, Edwin(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Called Strike	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-22	CH	86.0	1598	Wendelken, J.B.(R)	Alonso, Pete(R)	32.4	28°	56	
2-0	Top 6	Hit Into Play	
Pete Alonso grounds out softly to first baseman Christian Walker. Starling Marte scores.

2022-04-22	SI	95.1	2349	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso grounds out softly to first baseman Christian Walker. Starling Marte scores.

2022-04-22	SI	96.1	2377	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso grounds out softly to first baseman Christian Walker. Starling Marte scores.

2022-04-21	SI	90.9	1965	DeSclafani, Anthony(R)	Alonso, Pete(R)	106.3	0°	52	
3-2	Bot 5	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	KC	78.8	2045	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Ball	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	SI	90.7	2067	DeSclafani, Anthony(R)	Alonso, Pete(R)	66.8	-44°	3	
2-1	Bot 5	Foul	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	SL	86.7	2183	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
2-0	Bot 5	Called Strike	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	SI	91.1	2042	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Ball	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	SL	87.7	2227	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-21	SI	93.1	2156	DeSclafani, Anthony(R)	Alonso, Pete(R)	110.8	-6°	22	
0-0	Bot 3	Hit Into Play	
Pete Alonso grounds out, shortstop Brandon Crawford to first baseman Brandon Belt.

2022-04-21	SL	87.2	2107	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
0-2	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-21	SL	88.5	2213	DeSclafani, Anthony(R)	Alonso, Pete(R)	--	°		
0-1	Bot 1	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-21	SL	88.9	2251	DeSclafani, Anthony(R)	Alonso, Pete(R)	64.8	-21°	5	
0-0	Bot 1	Foul	
Pete Alonso strikes out swinging.

2022-04-21	FF	95.9	2056	Beede, Tyler(R)	Alonso, Pete(R)	98.6	8°	183	
2-1	Bot 7	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Mauricio Dubon.

2022-04-21	CU	77.9	1897	Beede, Tyler(R)	Alonso, Pete(R)	--	°		
1-1	Bot 7	Ball	
Pete Alonso singles on a line drive to center fielder Mauricio Dubon.

2022-04-21	CU	79.4	1889	Beede, Tyler(R)	Alonso, Pete(R)	--	°		
0-1	Bot 7	Ball	
Pete Alonso singles on a line drive to center fielder Mauricio Dubon.

2022-04-21	FF	94.9	2081	Beede, Tyler(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso singles on a line drive to center fielder Mauricio Dubon.

2022-04-20	FF	93.6	2253	Rodón, Carlos(L)	Alonso, Pete(R)	100.6	14°	218	
0-1	Bot 4	Hit Into Play	
Pete Alonso singles on a sharp line drive to left fielder Joc Pederson.

2022-04-20	SL	84.5	2227	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso singles on a sharp line drive to left fielder Joc Pederson.

2022-04-20	FF	95.4	2326	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
2-2	Bot 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-20	FF	95.1	2324	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
2-1	Bot 2	Swinging Strike	
Pete Alonso called out on strikes.

2022-04-20	FF	94.2	2321	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
2-0	Bot 2	Swinging Strike	
Pete Alonso called out on strikes.

2022-04-20	CU	77.4	2302	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
1-0	Bot 2	Ball	
Pete Alonso called out on strikes.

2022-04-20	FF	93.3	2340	Rodón, Carlos(L)	Alonso, Pete(R)	--	°		
0-0	Bot 2	Ball	
Pete Alonso called out on strikes.

2022-04-20	SL	81.2	2503	Brebbia, John(R)	Alonso, Pete(R)	70.0	45°	189	
0-0	Bot 6	Hit Into Play	
Pete Alonso singles on a fly ball to right fielder Mike Yastrzemski.

2022-04-20	FF	82.2	1917	Rogers, Tyler(R)	Alonso, Pete(R)	77.5	-11°	12	
0-0	Bot 8	Hit Into Play	
Pete Alonso singles on a ground ball to right fielder Mike Yastrzemski.

2022-04-19	SL	82.6	2562	Webb, Logan(R)	Alonso, Pete(R)	--	°		
3-2	Bot 3	Ball	
Pete Alonso walks.

2022-04-19	SI	91.2	1939	Webb, Logan(R)	Alonso, Pete(R)	--	°		
2-2	Bot 3	Ball	
Pete Alonso walks.

2022-04-19	CH	84.7	1476	Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-2	Bot 3	Ball	
Pete Alonso walks.

2022-04-19	CH	85.6	1576	Webb, Logan(R)	Alonso, Pete(R)	64.6	-47°	2	
1-2	Bot 3	Foul	
Pete Alonso walks.

2022-04-19	SL	83.0	2689	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-2	Bot 3	Blocked Ball	
Pete Alonso walks.

2022-04-19	FS	91.1	1475	Cobb, Alex(R)	Alonso, Pete(R)	87.5	-5°	15	
2-1	Bot 4	Hit Into Play	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	CH	85.4	1607	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-1	Bot 3	Swinging Strike Blocked	
Pete Alonso walks.

2022-04-19	FS	88.1	1710	Cobb, Alex(R)	Alonso, Pete(R)	54.8	-37°	3	
2-0	Bot 4	Foul	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	SL	81.6	2595	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Called Strike	
Pete Alonso walks.

2022-04-19	SI	94.8	2078	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
1-0	Bot 4	Ball	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	SI	95.7	2234	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Ball	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	FF	94.8	2195	Long, Sam(L)	Alonso, Pete(R)	--	°		
3-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-19	CH	83.6	1998	Long, Sam(L)	Alonso, Pete(R)	65.1	74°	113	
3-2	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-04-19	FF	92.9	2232	Long, Sam(L)	Alonso, Pete(R)	61.0	70°	107	
3-1	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-04-19	CH	81.7	1936	Long, Sam(L)	Alonso, Pete(R)	--	°		
2-1	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	CU	74.4	2541	Long, Sam(L)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	FF	92.9	2245	Long, Sam(L)	Alonso, Pete(R)	--	°		
1-0	Bot 5	Called Strike	
Pete Alonso strikes out swinging.

2022-04-19	FF	94.8	2251	Leone, Dominic(R)	Alonso, Pete(R)	--	°		
3-2	Bot 5	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-19	SI	95.5	2091	Cobb, Alex(R)	Alonso, Pete(R)	100.9	17°	305	
2-2	Bot 1	Hit Into Play	
Pete Alonso lines out sharply to right fielder Mike Yastrzemski.

2022-04-19	SI	91.2	1887	Webb, Logan(R)	Alonso, Pete(R)	63.3	-4°	20	
2-1	Bot 1	Hit Into Play	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	SI	93.9	2245	Long, Sam(L)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	SI	94.0	2042	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Ball	
Pete Alonso lines out sharply to right fielder Mike Yastrzemski.

2022-04-19	SL	84.3	2449	Leone, Dominic(R)	Alonso, Pete(R)	--	°		
2-2	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	FF	94.9	2254	Leone, Dominic(R)	Alonso, Pete(R)	73.6	34°	234	
2-1	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-04-19	SI	90.5	1851	Webb, Logan(R)	Alonso, Pete(R)	34.0	28°	59	
2-0	Bot 1	Foul	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	FS	88.7	1366	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Called Strike	
Pete Alonso lines out sharply to right fielder Mike Yastrzemski.

2022-04-19	FS	90.1	1455	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Called Strike	
Pete Alonso lines out sharply to right fielder Mike Yastrzemski.

2022-04-19	SI	90.7	1912	Webb, Logan(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	FC	90.4	2522	Leone, Dominic(R)	Alonso, Pete(R)	--	°		
1-1	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	FC	90.0	2332	Leone, Dominic(R)	Alonso, Pete(R)	70.3	-15°	8	
1-0	Bot 5	Foul	
Pete Alonso strikes out swinging.

2022-04-19	FF	83.6	1859	Rogers, Tyler(R)	Alonso, Pete(R)	--	°		
2-2	Bot 8	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-19	KC	85.8	2722	Cobb, Alex(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso lines out sharply to right fielder Mike Yastrzemski.

2022-04-19	SI	89.8	1928	Webb, Logan(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso grounds out, third baseman Jason Vosler to first baseman Brandon Belt.

2022-04-19	SL	71.4	2427	Rogers, Tyler(R)	Alonso, Pete(R)	45.3	68°	72	
2-2	Bot 8	Foul	
Pete Alonso strikes out swinging.

2022-04-19	SL	82.7	2374	Leone, Dominic(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Ball	
Pete Alonso strikes out swinging.

2022-04-19	FF	84.0	1984	Rogers, Tyler(R)	Alonso, Pete(R)	60.5	26°	129	
2-2	Bot 8	Foul	
Pete Alonso strikes out swinging.

2022-04-19	SL	72.1	2525	Rogers, Tyler(R)	Alonso, Pete(R)	55.0	67°	110	
2-2	Bot 8	Foul	
Pete Alonso strikes out swinging.

2022-04-19	SL	70.9	2446	Rogers, Tyler(R)	Alonso, Pete(R)	--	°		
2-1	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-04-19	FF	83.1	2034	Rogers, Tyler(R)	Alonso, Pete(R)	--	°		
1-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-04-19	SL	72.1	2401	Rogers, Tyler(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Ball	
Pete Alonso strikes out swinging.

2022-04-19	FF	83.1	1909	Rogers, Tyler(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso strikes out swinging.

2022-04-19	SL	83.6	2682	Marte, Yunior(R)	Alonso, Pete(R)	55.3	31°	132	
0-2	Bot 8	Hit Into Play	
Pete Alonso singles on a soft line drive to first baseman Brandon Belt.

2022-04-19	SI	96.4	2188	Marte, Yunior(R)	Alonso, Pete(R)	--	°		
0-1	Bot 8	Swinging Strike	
Pete Alonso singles on a soft line drive to first baseman Brandon Belt.

2022-04-19	FF	97.6	2304	Marte, Yunior(R)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Called Strike	
Pete Alonso singles on a soft line drive to first baseman Brandon Belt.

2022-04-17	SI	89.5	2037	Castellanos, Humberto(R)	Alonso, Pete(R)	96.5	47°	242	
1-1	Bot 3	Hit Into Play	
Pete Alonso pops out to second baseman Ketel Marte.

2022-04-17	CU	75.9	2338	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
1-0	Bot 3	Called Strike	
Pete Alonso pops out to second baseman Ketel Marte.

2022-04-17	CU	77.9	2362	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
0-0	Bot 3	Ball	
Pete Alonso pops out to second baseman Ketel Marte.

2022-04-17	CU	74.4	2346	Castellanos, Humberto(R)	Alonso, Pete(R)	87.6	30°	304	
3-1	Bot 1	Hit Into Play	
Pete Alonso flies out to center fielder Jake McCarthy.

2022-04-17	SI	89.2	2049	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
3-0	Bot 1	Called Strike	
Pete Alonso flies out to center fielder Jake McCarthy.

2022-04-17	SI	89.5	1984	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
2-0	Bot 1	Ball	
Pete Alonso flies out to center fielder Jake McCarthy.

2022-04-17	SI	90.2	2047	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
1-0	Bot 1	Ball	
Pete Alonso flies out to center fielder Jake McCarthy.

2022-04-17	CU	76.6	2447	Castellanos, Humberto(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out to center fielder Jake McCarthy.

2022-04-17	SI	92.8	2037	Peacock, Matt(R)	Alonso, Pete(R)	111.6	17°	408	
1-2	Bot 7	Hit Into Play	
Pete Alonso homers (3) on a line drive to left center field. Francisco Lindor scores.

2022-04-17	CH	82.0	2066	Ramirez, Noé(R)	Alonso, Pete(R)	68.1	63°	108	
2-2	Bot 6	Hit Into Play	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	CH	83.6	1674	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
1-2	Bot 6	Ball	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	SL	85.3	2635	Peacock, Matt(R)	Alonso, Pete(R)	--	°		
0-2	Bot 7	Ball	
Pete Alonso homers (3) on a line drive to left center field. Francisco Lindor scores.

2022-04-17	SI	90.8	1857	Peacock, Matt(R)	Alonso, Pete(R)	72.5	-30°	4	
0-1	Bot 7	Foul	
Pete Alonso homers (3) on a line drive to left center field. Francisco Lindor scores.

2022-04-17	CH	82.0	1678	Ramirez, Noé(R)	Alonso, Pete(R)	93.2	-41°	3	
1-2	Bot 6	Foul	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	SI	91.2	1943	Peacock, Matt(R)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Called Strike	
Pete Alonso homers (3) on a line drive to left center field. Francisco Lindor scores.

2022-04-17	FF	88.8	2100	Ramirez, Noé(R)	Alonso, Pete(R)	69.7	60°	194	
1-2	Bot 6	Foul	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	CU	78.7	2560	Ramirez, Noé(R)	Alonso, Pete(R)	64.5	15°	119	
1-1	Bot 6	Foul	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	FF	88.7	2182	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
1-0	Bot 6	Called Strike	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-17	CU	78.5	2427	Ramirez, Noé(R)	Alonso, Pete(R)	--	°		
0-0	Bot 6	Ball	
Pete Alonso pops into a force out, shortstop Geraldo Perdomo to second baseman Ketel Marte. Francisco Lindor out at 2nd. Pete Alonso to 1st.

2022-04-16	FF	92.6	2410	Gallen, Zac(R)	Alonso, Pete(R)	72.7	70°	89	
1-2	Bot 4	Hit Into Play	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	KC	79.9	2308	Gallen, Zac(R)	Alonso, Pete(R)	53.2	49°	131	
1-2	Bot 4	Foul	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	CH	83.5	1448	Gallen, Zac(R)	Alonso, Pete(R)	91.4	18°	234	
1-2	Bot 4	Foul	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	FF	90.9	2241	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-2	Bot 4	Ball	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	CH	81.7	1385	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-1	Bot 4	Swinging Strike Blocked	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	KC	77.7	2224	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-0	Bot 4	Called Strike	
Pete Alonso pops out to first baseman Christian Walker.

2022-04-16	FF	94.8	2486	Gallen, Zac(R)	Alonso, Pete(R)	100.8	35°	336	
2-2	Bot 1	Hit Into Play	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-16	FF	92.6	2485	Kennedy, Ian(R)	Alonso, Pete(R)	81.4	-5°	23	
0-0	Bot 8	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Sergio Alcantara to second baseman Ketel Marte to first baseman Christian Walker. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-16	CH	86.9	1535	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
1-2	Bot 1	Blocked Ball	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-16	FF	92.8	2386	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
1-1	Bot 1	Swinging Strike	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-16	FF	93.5	2335	Gallen, Zac(R)	Alonso, Pete(R)	64.9	34°	170	
1-0	Bot 1	Foul	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-16	FF	94.0	2438	Gallen, Zac(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Ball	
Pete Alonso flies out to right fielder Pavin Smith.

2022-04-16	SI	94.8	2132	Poppen, Sean(R)	Alonso, Pete(R)	90.8	31°	325	
0-0	Bot 6	Hit Into Play	
Pete Alonso flies out to left fielder David Peralta.

2022-04-15	FF	92.1	2521	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
3-1	Bot 8	Ball	
Pete Alonso walks.

2022-04-15	FF	91.9	2455	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
3-0	Bot 8	Called Strike	
Pete Alonso walks.

2022-04-15	FF	92.2	2497	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
2-0	Bot 8	Ball	
Pete Alonso walks.

2022-04-15	CH	85.3	2056	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
1-0	Bot 8	Ball	
Pete Alonso walks.

2022-04-15	SL	86.4	2392	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
0-0	Bot 8	Ball	
Pete Alonso walks.

2022-04-15	CH	78.8	1491	Davies, Zach(R)	Alonso, Pete(R)	93.2	48°	274	
0-0	Bot 3	Hit Into Play	
Pete Alonso out on a sacrifice fly to left fielder David Peralta. Starling Marte scores.

2022-04-15	FF	92.2	2527	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
3-2	Bot 7	Called Strike	
Pete Alonso called out on strikes.

2022-04-15	SL	86.5	2323	Smith, Caleb(L)	Alonso, Pete(R)	104.4	8°	156	
3-2	Bot 7	Foul	
Pete Alonso called out on strikes.

2022-04-15	SL	86.1	2360	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
2-2	Bot 7	Ball	
Pete Alonso called out on strikes.

2022-04-15	FF	91.5	2485	Smith, Caleb(L)	Alonso, Pete(R)	76.8	73°	148	
2-1	Bot 7	Foul	
Pete Alonso called out on strikes.

2022-04-15	FF	91.5	2441	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
2-0	Bot 7	Foul Tip	
Pete Alonso called out on strikes.

2022-04-15	FF	92.3	2505	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
1-0	Bot 7	Ball	
Pete Alonso called out on strikes.

2022-04-15	FF	91.8	2512	Smith, Caleb(L)	Alonso, Pete(R)	--	°		
0-0	Bot 7	Ball	
Pete Alonso called out on strikes.

2022-04-15	SI	87.1	1860	Davies, Zach(R)	Alonso, Pete(R)	91.9	49°	246	
1-0	Bot 1	Hit Into Play	
Pete Alonso out on a sacrifice fly to left fielder David Peralta in foul territory. Jeff McNeil scores. Francisco Lindor to 2nd.

2022-04-15	SI	87.9	1886	Davies, Zach(R)	Alonso, Pete(R)	--	°		
0-0	Bot 1	Blocked Ball	
Pete Alonso out on a sacrifice fly to left fielder David Peralta in foul territory. Jeff McNeil scores. Francisco Lindor to 2nd.

2022-04-15	SL	83.9	2587	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
1-2	Bot 5	Hit By Pitch	
Pete Alonso hit by pitch.

2022-04-15	CH	84.2	1557	Wendelken, J.B.(R)	Alonso, Pete(R)	64.9	78°	97	
1-2	Bot 5	Foul	
Pete Alonso hit by pitch.

2022-04-15	SI	91.8	2379	Wendelken, J.B.(R)	Alonso, Pete(R)	80.5	59°	213	
1-1	Bot 5	Foul	
Pete Alonso hit by pitch.

2022-04-15	SL	88.8	2613	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
0-1	Bot 5	Ball	
Pete Alonso hit by pitch.

2022-04-15	SL	84.6	2585	Wendelken, J.B.(R)	Alonso, Pete(R)	--	°		
0-0	Bot 5	Called Strike	
Pete Alonso hit by pitch.

2022-04-13	CH	83.2	1398	Nola, Aaron(R)	Alonso, Pete(R)	110.9	15°	282	
0-2	Top 4	Hit Into Play	
Pete Alonso doubles (2) on a sharp line drive to left fielder Nick Castellanos. Starling Marte scores.

2022-04-13	FF	93.2	2257	Nola, Aaron(R)	Alonso, Pete(R)	72.4	30°	218	
0-2	Top 4	Foul	
Pete Alonso doubles (2) on a sharp line drive to left fielder Nick Castellanos. Starling Marte scores.

2022-04-13	FF	91.8	2219	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Swinging Strike	
Pete Alonso doubles (2) on a sharp line drive to left fielder Nick Castellanos. Starling Marte scores.

2022-04-13	SI	88.3	2119	Nola, Aaron(R)	Alonso, Pete(R)	100.1	29°	359	
0-0	Top 4	Foul	
Pete Alonso doubles (2) on a sharp line drive to left fielder Nick Castellanos. Starling Marte scores.

2022-04-13	FF	87.8	1560	Falter, Bailey(L)	Alonso, Pete(R)	95.3	-9°	17	
2-1	Top 9	Hit Into Play	
Pete Alonso grounds out, shortstop Didi Gregorius to first baseman Alec Bohm.

2022-04-13	FF	89.4	1575	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
1-1	Top 9	Ball	
Pete Alonso grounds out, shortstop Didi Gregorius to first baseman Alec Bohm.

2022-04-13	FF	89.8	1609	Falter, Bailey(L)	Alonso, Pete(R)	78.6	33°	236	
1-0	Top 9	Foul	
Pete Alonso grounds out, shortstop Didi Gregorius to first baseman Alec Bohm.

2022-04-13	CH	78.4	964	Falter, Bailey(L)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso grounds out, shortstop Didi Gregorius to first baseman Alec Bohm.

2022-04-13	SL	85.6	2475	Domínguez, Seranthony(R)	Alonso, Pete(R)	99.7	28°	386	
1-2	Top 5	Hit Into Play	
Pete Alonso doubles (3) on a fly ball to center fielder Matt Vierling. Francisco Lindor scores.

2022-04-13	FF	95.7	2410	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
1-1	Top 5	Foul Tip	
Pete Alonso doubles (3) on a fly ball to center fielder Matt Vierling. Francisco Lindor scores.

2022-04-13	SL	84.7	2408	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
0-1	Top 5	Ball	
Pete Alonso doubles (3) on a fly ball to center fielder Matt Vierling. Francisco Lindor scores.

2022-04-13	SL	85.8	2407	Domínguez, Seranthony(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Called Strike	
Pete Alonso doubles (3) on a fly ball to center fielder Matt Vierling. Francisco Lindor scores.

2022-04-13	SI	92.2	2131	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-2	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-13	KC	78.0	2460	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-1	Top 2	Swinging Strike	
Pete Alonso called out on strikes.

2022-04-13	FF	92.5	2244	Nola, Aaron(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Called Strike	
Pete Alonso called out on strikes.

2022-04-13	FF	94.7	2210	Brogdon, Connor(R)	Alonso, Pete(R)	103.0	27°	398	
2-2	Top 6	Hit Into Play	
Pete Alonso homers (2) on a fly ball to right center field. Francisco Lindor scores. Starling Marte scores.

2022-04-13	FF	94.2	2176	Brogdon, Connor(R)	Alonso, Pete(R)	74.7	51°	200	
2-1	Top 6	Foul	
Pete Alonso homers (2) on a fly ball to right center field. Francisco Lindor scores. Starling Marte scores.

2022-04-13	CH	82.2	1664	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
1-1	Top 6	Ball	
Pete Alonso homers (2) on a fly ball to right center field. Francisco Lindor scores. Starling Marte scores.

2022-04-13	FF	93.6	2146	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
1-0	Top 6	Swinging Strike	
Pete Alonso homers (2) on a fly ball to right center field. Francisco Lindor scores. Starling Marte scores.

2022-04-13	FF	93.9	2189	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso homers (2) on a fly ball to right center field. Francisco Lindor scores. Starling Marte scores.

2022-04-12	SI	93.9	2158	Wheeler, Zack(R)	Alonso, Pete(R)	96.2	1°	52	
0-0	Top 4	Hit Into Play	
Pete Alonso singles on a ground ball to left fielder Kyle Schwarber.

2022-04-12	SI	93.7	2009	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
3-2	Top 6	Called Strike	
Pete Alonso called out on strikes.

2022-04-12	CH	83.8	1650	Sánchez, Cristopher(L)	Alonso, Pete(R)	86.3	26°	249	
3-2	Top 6	Foul	
Pete Alonso called out on strikes.

2022-04-12	SI	95.2	2178	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
3-2	Top 1	Hit By Pitch	
Pete Alonso hit by pitch.

2022-04-12	SI	93.6	2003	Sánchez, Cristopher(L)	Alonso, Pete(R)	74.5	49°	206	
3-1	Top 6	Foul	
Pete Alonso called out on strikes.

2022-04-12	SI	95.2	2192	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
2-2	Top 1	Ball	
Pete Alonso hit by pitch.

2022-04-12	SI	93.3	2057	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
3-0	Top 6	Called Strike	
Pete Alonso called out on strikes.

2022-04-12	FF	95.5	2277	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Ball	
Pete Alonso hit by pitch.

2022-04-12	SI	95.2	2234	Wheeler, Zack(R)	Alonso, Pete(R)	64.2	73°	104	
1-1	Top 1	Foul	
Pete Alonso hit by pitch.

2022-04-12	SI	94.4	2101	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
2-0	Top 6	Ball	
Pete Alonso called out on strikes.

2022-04-12	FF	95.8	2353	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Called Strike	
Pete Alonso hit by pitch.

2022-04-12	SI	94.0	2084	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
1-0	Top 6	Ball	
Pete Alonso called out on strikes.

2022-04-12	SI	94.3	2204	Wheeler, Zack(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso hit by pitch.

2022-04-12	CH	85.7	1775	Sánchez, Cristopher(L)	Alonso, Pete(R)	--	°		
0-0	Top 6	Ball	
Pete Alonso called out on strikes.

2022-04-12	FF	93.5	2239	Brogdon, Connor(R)	Alonso, Pete(R)	85.0	49°	247	
3-1	Top 8	Hit Into Play	
Pete Alonso flies out to center fielder Simon Muzziotti.

2022-04-12	FC	87.9	2297	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
2-1	Top 8	Ball	
Pete Alonso flies out to center fielder Simon Muzziotti.

2022-04-12	CH	81.4	1736	Brogdon, Connor(R)	Alonso, Pete(R)	66.0	-32°	5	
2-0	Top 8	Foul	
Pete Alonso flies out to center fielder Simon Muzziotti.

2022-04-12	FF	93.5	2239	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
1-0	Top 8	Ball	
Pete Alonso flies out to center fielder Simon Muzziotti.

2022-04-12	CH	80.9	1781	Brogdon, Connor(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso flies out to center fielder Simon Muzziotti.

2022-04-11	CH	86.3	1644	Suárez, Ranger(L)	Alonso, Pete(R)	53.1	-35°	1	
1-2	Top 3	Hit Into Play	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso reaches on a throwing error by third baseman Alec Bohm.

2022-04-11	CH	87.3	1610	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-2	Top 3	Ball	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso reaches on a throwing error by third baseman Alec Bohm.

2022-04-11	FF	92.7	1803	Suárez, Ranger(L)	Alonso, Pete(R)	113.7	37°	410	
0-1	Top 3	Foul	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso reaches on a throwing error by third baseman Alec Bohm.

2022-04-11	CH	83.4	1402	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-0	Top 3	Called Strike	
Mets challenged (play at 1st), call on the field was overturned: Pete Alonso reaches on a throwing error by third baseman Alec Bohm.

2022-04-11	FF	96.3	1994	Nelson, Nick(R)	Alonso, Pete(R)	93.5	36°	312	
1-1	Top 5	Hit Into Play	
Pete Alonso flies out to right fielder Bryce Harper.

2022-04-11	CH	89.7	1830	Nelson, Nick(R)	Alonso, Pete(R)	77.5	-55°	1	
1-0	Top 5	Foul	
Pete Alonso flies out to right fielder Bryce Harper.

2022-04-11	FF	96.1	1982	Nelson, Nick(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso flies out to right fielder Bryce Harper.

2022-04-11	CH	86.8	1569	Suárez, Ranger(L)	Alonso, Pete(R)	95.3	-16°	5	
1-1	Top 1	Hit Into Play	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins. Brandon Nimmo scores. Starling Marte to 3rd.

2022-04-11	CH	85.1	1582	Suárez, Ranger(L)	Alonso, Pete(R)	84.9	-28°	3	
1-0	Top 1	Foul	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins. Brandon Nimmo scores. Starling Marte to 3rd.

2022-04-11	FF	93.6	1854	Suárez, Ranger(L)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso grounds out, third baseman Alec Bohm to first baseman Rhys Hoskins. Brandon Nimmo scores. Starling Marte to 3rd.

2022-04-11	SL	85.8	2483	Domínguez, Seranthony(R)	Alonso, Pete(R)	99.6	18°	288	
0-0	Top 7	Hit Into Play	
Pete Alonso lines out to left fielder Kyle Schwarber.

2022-04-10	FC	88.7	2172	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
2-2	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-10	CU	81.3	2337	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
2-1	Top 4	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-10	CH	86.9	1742	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-04-10	CU	78.7	2312	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-1	Top 4	Ball	
Pete Alonso strikes out swinging.

2022-04-10	FC	87.7	2209	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Called Strike	
Pete Alonso strikes out swinging.

2022-04-10	SI	93.0	1847	Fedde, Erick(R)	Alonso, Pete(R)	103.5	-3°	31	
2-0	Top 2	Hit Into Play	
Pete Alonso grounds out, shortstop Lucius Fox to first baseman Josh Bell.

2022-04-10	CU	78.2	2207	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso grounds out, shortstop Lucius Fox to first baseman Josh Bell.

2022-04-10	SI	92.1	1751	Fedde, Erick(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso grounds out, shortstop Lucius Fox to first baseman Josh Bell.

2022-04-10	SI	95.3	2031	Finnegan, Kyle(R)	Alonso, Pete(R)	108.6	3°	99	
1-0	Top 8	Hit Into Play	
Pete Alonso lines out, pitcher Kyle Finnegan to first baseman Josh Bell.

2022-04-10	SL	75.9	2221	Cishek, Steve(R)	Alonso, Pete(R)	83.0	4°	65	
0-0	Top 6	Hit Into Play	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-04-10	SL	87.3	2113	Finnegan, Kyle(R)	Alonso, Pete(R)	--	°		
0-0	Top 8	Ball	
Pete Alonso lines out, pitcher Kyle Finnegan to first baseman Josh Bell.

2022-04-09	FF	91.2	2088	Adon, Joan(R)	Alonso, Pete(R)	111.6	39°	358	
2-1	Top 5	Hit Into Play	
Pete Alonso hits a grand slam (1) to left field. James McCann scores. Brandon Nimmo scores. Francisco Lindor scores.

2022-04-09	FF	92.5	2133	Adon, Joan(R)	Alonso, Pete(R)	--	°		
2-0	Top 5	Called Strike	
Pete Alonso hits a grand slam (1) to left field. James McCann scores. Brandon Nimmo scores. Francisco Lindor scores.

2022-04-09	FF	92.1	2070	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-0	Top 5	Ball	
Pete Alonso hits a grand slam (1) to left field. James McCann scores. Brandon Nimmo scores. Francisco Lindor scores.

2022-04-09	FF	93.1	2084	Adon, Joan(R)	Alonso, Pete(R)	--	°		
0-0	Top 5	Ball	
Pete Alonso hits a grand slam (1) to left field. James McCann scores. Brandon Nimmo scores. Francisco Lindor scores.

2022-04-09	FF	92.1	2048	Adon, Joan(R)	Alonso, Pete(R)	109.9	17°	387	
0-0	Top 3	Hit Into Play	
Pete Alonso lines out sharply to center fielder Victor Robles.

2022-04-09	FF	96.1	2219	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-09	SL	86.8	2093	Machado, Andrés(R)	Alonso, Pete(R)	77.1	64°	163	
2-2	Top 9	Foul	
Pete Alonso strikes out swinging.

2022-04-09	SL	86.5	2062	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
2-1	Top 9	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-09	SL	86.8	2088	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
2-0	Top 9	Called Strike	
Pete Alonso strikes out swinging.

2022-04-09	SL	87.4	2100	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
1-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-04-09	SI	94.5	2044	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Ball	
Pete Alonso strikes out swinging.

2022-04-09	CU	82.7	2168	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-2	Top 1	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-04-09	FF	94.9	2128	Adon, Joan(R)	Alonso, Pete(R)	90.4	14°	174	
1-1	Top 1	Foul	
Pete Alonso strikes out swinging.

2022-04-09	FF	95.0	2130	Adon, Joan(R)	Alonso, Pete(R)	--	°		
1-0	Top 1	Called Strike	
Pete Alonso strikes out swinging.

2022-04-09	FF	93.6	2035	Adon, Joan(R)	Alonso, Pete(R)	--	°		
0-0	Top 1	Ball	
Pete Alonso strikes out swinging.

2022-04-09	SL	85.7	2377	Rainey, Tanner(R)	Alonso, Pete(R)	--	°		
1-2	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-09	SL	87.3	2365	Rainey, Tanner(R)	Alonso, Pete(R)	--	°		
0-2	Top 7	Ball	
Pete Alonso strikes out swinging.

2022-04-09	SL	87.0	2326	Rainey, Tanner(R)	Alonso, Pete(R)	--	°		
0-1	Top 7	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-09	FF	94.9	2345	Rainey, Tanner(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Called Strike	
Pete Alonso strikes out swinging.

2022-04-08	SL	85.1	2026	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-2	Top 4	Called Strike	
Pete Alonso called out on strikes.

2022-04-08	SL	83.7	2072	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-2	Top 4	Blocked Ball	
Pete Alonso called out on strikes.

2022-04-08	SL	84.5	2029	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-1	Top 4	Swinging Strike	
Pete Alonso called out on strikes.

2022-04-08	SL	84.4	2036	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-0	Top 4	Swinging Strike	
Pete Alonso called out on strikes.

2022-04-08	FF	92.2	2158	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
0-0	Top 4	Ball	
Pete Alonso called out on strikes.

2022-04-08	CU	82.8	2532	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-2	Top 2	Swinging Strike Blocked	
Pete Alonso strikes out swinging.

2022-04-08	FF	93.5	2140	Gray, Josiah(R)	Alonso, Pete(R)	77.4	82°	106	
2-2	Top 2	Foul	
Pete Alonso strikes out swinging.

2022-04-08	FF	93.2	2166	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-1	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-08	ST	76.7	2599	Espino, Paolo(R)	Alonso, Pete(R)	113.5	18°	358	
0-1	Top 9	Hit Into Play	
Pete Alonso doubles (1) on a sharp line drive to left fielder Yadiel Hernandez.

2022-04-08	ST	77.8	2588	Espino, Paolo(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso doubles (1) on a sharp line drive to left fielder Yadiel Hernandez.

2022-04-08	FF	93.8	2219	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
2-0	Top 2	Swinging Strike	
Pete Alonso strikes out swinging.

2022-04-08	SL	84.4	2026	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
1-0	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-04-08	SL	84.1	2092	Gray, Josiah(R)	Alonso, Pete(R)	--	°		
0-0	Top 2	Ball	
Pete Alonso strikes out swinging.

2022-04-08	FF	93.7	2187	Doolittle, Sean(L)	Alonso, Pete(R)	97.0	69°	125	
0-0	Top 5	Hit Into Play	
Pete Alonso pops out to first baseman Josh Bell on the infield fly rule.

2022-04-08	FF	94.5	2136	Murphy, Patrick(R)	Alonso, Pete(R)	91.3	-23°	6	
0-0	Top 7	Hit Into Play	
Pete Alonso grounds out, third baseman Maikel Franco to first baseman Josh Bell.

2022-04-07	CH	82.6	1573	Corbin, Patrick(L)	Alonso, Pete(R)	89.9	15°	244	
0-0	Top 4	Hit Into Play	
Pete Alonso singles on a line drive to center fielder Victor Robles.

2022-04-07	FF	90.5	1913	Corbin, Patrick(L)	Alonso, Pete(R)	72.4	48°	199	
3-2	Top 1	Hit Into Play	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SL	87.0	1938	Machado, Andrés(R)	Alonso, Pete(R)	51.2	14°	64	
2-2	Top 7	Hit Into Play	
Pete Alonso grounds into a double play, shortstop Alcides Escobar to second baseman Cesar Hernandez to first baseman Josh Bell. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-07	SL	86.2	1895	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
2-1	Top 7	Called Strike	
Pete Alonso grounds into a double play, shortstop Alcides Escobar to second baseman Cesar Hernandez to first baseman Josh Bell. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-07	SL	82.9	2226	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
2-2	Top 1	Blocked Ball	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SL	80.8	2228	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
1-2	Top 1	Blocked Ball	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SI	94.4	2151	Machado, Andrés(R)	Alonso, Pete(R)	66.9	-26°	3	
2-0	Top 7	Foul	
Pete Alonso grounds into a double play, shortstop Alcides Escobar to second baseman Cesar Hernandez to first baseman Josh Bell. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-07	FF	93.2	2142	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
1-0	Top 7	Ball	
Pete Alonso grounds into a double play, shortstop Alcides Escobar to second baseman Cesar Hernandez to first baseman Josh Bell. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-07	SI	92.3	2066	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-2	Top 1	Ball	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SI	94.9	2091	Thompson, Mason(R)	Alonso, Pete(R)	--	°		
2-2	Top 9	Hit By Pitch	
Pete Alonso hit by pitch.

2022-04-07	FF	91.0	2077	Corbin, Patrick(L)	Alonso, Pete(R)	--	°		
0-1	Top 1	Called Strike	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SI	94.3	1980	Machado, Andrés(R)	Alonso, Pete(R)	--	°		
0-0	Top 7	Ball	
Pete Alonso grounds into a double play, shortstop Alcides Escobar to second baseman Cesar Hernandez to first baseman Josh Bell. Francisco Lindor out at 2nd. Pete Alonso out at 1st.

2022-04-07	SL	85.7	2239	Thompson, Mason(R)	Alonso, Pete(R)	--	°		
1-2	Top 9	Ball	
Pete Alonso hit by pitch.

2022-04-07	SL	86.2	2288	Thompson, Mason(R)	Alonso, Pete(R)	--	°		
0-2	Top 9	Ball	
Pete Alonso hit by pitch.

2022-04-07	FF	90.8	2172	Corbin, Patrick(L)	Alonso, Pete(R)	69.9	45°	191	
0-0	Top 1	Foul	
Pete Alonso flies out to shortstop Alcides Escobar.

2022-04-07	SI	96.6	2207	Thompson, Mason(R)	Alonso, Pete(R)	71.8	27°	211	
0-1	Top 9	Foul	
Pete Alonso hit by pitch.

2022-04-07	SL	84.4	2166	Thompson, Mason(R)	Alonso, Pete(R)	--	°		
0-0	Top 9	Called Strike	
Pete Alonso hit by pitch.

2022-04-07	FF	93.5	2224	Voth, Austin(R)	Alonso, Pete(R)	68.5	23°	193	
1-2	Top 6	Hit Into Play	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-04-07	CU	78.3	2937	Voth, Austin(R)	Alonso, Pete(R)	--	°		
0-2	Top 6	Ball	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-04-07	FF	92.3	2217	Voth, Austin(R)	Alonso, Pete(R)	--	°		
0-1	Top 6	Called Strike	
Pete Alonso singles on a line drive to right fielder Juan Soto.

2022-04-07	FF	93.5	2392	Voth, Austin(R)	Alonso, Pete(R)	70.5	62°	175	
0-0	Top 6	Foul	
Pete Alonso singles on a line drive to right fielder Juan Soto.


'''

# Process the text data and convert it into rows
num_columns = 13

rows = []
current_row = []
for line in text_data.split('\n'):
    line = line.strip()
    if line:
        current_row.extend(line.split('\t'))
    else:
        # Add empty values to the current row to match the original number of columns
        while len(current_row) < num_columns:
            current_row.append('')
        rows.append(current_row)
        current_row = []

# Add empty values to the last current_row, if necessary
while len(current_row) < num_columns:
    current_row.append('')
rows.append(current_row)

# Write the rows to a CSV file
with open('basa.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)




