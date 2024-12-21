# MH1402 - Algorithms and Computing II， Lab4， WK12
# Matric Number: Not Sure
# Author: Guo Jian

# IMPLEMENT HERE #
def MergeSort(mylist):
    # split the problem
    if len(mylist)>1:
        mid = len(mylist)//2
        left = mylist[:mid]
        right = mylist[mid:]

        MergeSort(left)
        MergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k]=left[i]
                i=i+1
            else:
                mylist[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            mylist[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            mylist[k]=right[j]
            j=j+1
            k=k+1

# IMPLEMENT HERE #
def QuickSort(mylist):
    if len(mylist) <= 1:
        return
    ll = []
    le = []
    lg = []
    i = 0;
    while i < len(mylist):
        if mylist[i] < mylist[-1]:
            ll.append(mylist[i])
        elif mylist[i] > mylist[-1]:
            lg.append(mylist[i])
        else:
            le.append(mylist[i])
        i += 1
    
    QuickSort(ll)
    QuickSort(lg)
    k = 0
    i = 0
    while i < len(ll):
        mylist[k] = ll[i]
        k += 1
        i += 1
    i = 0
    while i < len(le):
        mylist[k] = le[i]
        k += 1
        i += 1
    i = 0
    while i < len(lg):
        mylist[k] = lg[i]
        k += 1
        i += 1

# ----- test codes -----
mylist = [666, 223, 32, 724, 428, 893, 998, 910, 964, 853, 264, 955, 495, 191, 825, 879, 56, 544, 455, 611, 453, 926, 39, 845, 468, 3, 785, 513, 568, 108, 642, 817, 385, 136, 838, 30, 824, 768, 584, 387, 286, 25, 793, 552, 189, 40, 910, 880, 842, 189, 15, 425, 364, 757, 58, 828, 180, 386, 421, 189, 808, 877, 995, 414, 863, 66, 954, 826, 241, 36, 584, 553, 837, 812, 56, 617, 32, 486, 33, 116, 117, 393, 84, 215, 472, 268, 529, 862, 717, 880, 762, 482, 895, 418, 864, 237, 846, 72, 827, 324, 732, 280, 77, 945, 693, 825, 74, 597, 752, 553, 95, 428, 685, 711, 460, 265, 896, 630, 155, 919, 999, 375, 777, 567, 362, 8, 663, 98, 771, 954, 712, 877, 825, 829, 274, 40, 111, 541, 111, 832, 287, 302, 902, 617, 934, 230, 747, 766, 694, 255, 593, 863, 544, 585, 326, 835, 638, 394, 60, 504, 428, 730, 821, 92, 584, 61, 648, 815, 728, 222, 275, 155, 619, 587, 462, 480, 885, 918, 200, 492, 840, 107, 508, 385, 390, 66, 235, 967, 848, 421, 452, 966, 502, 936, 972, 476, 104, 209, 23, 661, 86, 309, 839, 509, 650, 406, 974, 329, 853, 575, 173, 326, 492, 411, 699, 91, 226, 217, 602, 53, 101, 104, 927, 23, 514, 255, 852, 495, 655, 566, 41, 703, 135, 807, 368, 601, 580, 876, 897, 819, 655, 837, 779, 812, 240, 999, 124, 134, 963, 916, 319, 138, 175, 18, 975, 872, 921, 628, 827, 375, 149, 466, 471, 107, 866, 16, 762, 270, 732, 655, 974, 136, 986, 684, 602, 875, 293, 384, 360, 459, 50, 399, 144, 86, 555, 402, 480, 925, 992, 438, 681, 38, 553, 32, 20, 488, 470, 147, 530, 780, 330, 39, 985, 622, 464, 894, 541, 745, 947, 144, 863, 362, 510, 655, 558, 551, 453, 332, 80, 563, 19, 157, 597, 471, 871, 947, 870, 954, 215, 354, 88, 242, 837, 692, 260, 500, 266, 450, 696, 807, 806, 996, 900, 574, 706, 860, 258, 470, 832, 728, 546, 537, 255, 275, 728, 593, 254, 576, 811, 359, 196, 380, 871, 768, 464, 87, 644, 216, 226, 429, 251, 501, 507, 152, 853, 152, 724, 940, 477, 31, 376, 493, 264, 397, 180, 26, 823, 914, 264, 348, 876, 658, 456, 289, 111, 587, 134, 972, 469, 477, 136, 345, 130, 269, 682, 534, 72, 920, 805, 366, 520, 994, 872, 515, 809, 346, 358, 623, 826, 22, 3, 182, 684, 166, 813, 609, 606, 922, 669, 553, 305, 610, 272, 632, 688, 690, 196, 459, 885, 560, 979, 44, 386, 163, 563, 355, 34, 133, 757, 537, 177, 940, 649, 59, 8, 733, 72, 636, 392, 21, 536, 780, 802, 999, 495, 667, 494, 489, 540, 859, 991, 494, 919, 260, 314, 610, 442, 381, 945, 982, 212, 650, 973, 195, 211, 160, 527, 655, 811, 303, 663, 349, 327, 782, 169, 179, 356, 477, 736, 729, 415, 187, 598, 430, 935, 23, 109, 236, 743, 726, 500, 403, 116, 735, 558, 819, 253, 655, 737, 264, 76, 212, 491, 755, 660, 805, 830, 452, 503, 42, 23, 340, 572, 236, 450, 455, 910, 245, 985, 444, 874, 522, 247, 778, 92, 348, 863, 120, 294, 78, 351, 728, 349, 504, 455, 421, 685, 455, 777, 567, 465, 562, 65, 111, 725, 23, 881, 427, 605, 153, 878, 269, 259, 415, 152, 674, 396, 515, 753, 596, 106, 824, 31, 651, 724, 364, 791, 418, 588, 860, 424, 470, 96, 487, 571, 938, 493, 319, 373, 662, 662, 577, 753, 287, 762, 851, 359, 948, 136, 535, 454, 811, 789, 242, 615, 767, 388, 876, 261, 373, 392, 823, 268, 250, 971, 210, 590, 452, 429, 130, 878, 842, 236, 193, 269, 508, 730, 704, 811, 800, 937, 635, 542, 908, 187, 513, 372, 781, 86, 339, 90, 829, 25, 410, 28, 424, 392, 506, 701, 507, 300, 197, 225, 186, 313, 39, 947, 810, 819, 765, 430, 14, 644, 147, 187, 127, 457, 65, 566, 428, 309, 378, 965, 928, 758, 597, 990, 686, 900, 794, 74, 970, 256, 104, 894, 820, 740, 557, 454, 325, 548, 473, 967, 72, 533, 354, 101, 210, 499, 816, 52, 600, 954, 281, 575, 415, 499, 46, 286, 396, 684, 312, 138, 783, 196, 492, 536, 496, 863, 278, 902, 678, 527, 807, 355, 70, 580, 751, 37, 230, 999, 945, 954, 981, 167, 199, 973, 780, 564, 762, 357, 935, 912, 726, 84, 234, 794, 490, 241, 441, 401, 928, 372, 271, 82, 273, 733, 729, 602, 235, 775, 769, 450, 955, 984, 45, 124, 273, 537, 217, 636, 797, 582, 406, 232, 455, 917, 13, 547, 839, 128, 566, 916, 477, 642, 317, 828, 428, 347, 880, 614, 801, 149, 536, 576, 615, 77, 178, 503, 503, 171, 792, 228, 996, 52, 468, 205, 768, 580, 721, 678, 329, 397, 277, 861, 389, 988, 732, 569, 235, 412, 892, 40, 937, 493, 989, 995, 349, 751, 193, 272, 15, 171, 779, 41, 327, 183, 99, 457, 171, 548, 352, 760, 481, 515, 983, 305, 567, 806, 250, 472, 896, 340, 754, 26, 832, 806, 663, 511, 380, 385, 191, 285, 676, 153, 447, 281, 267, 428, 688, 875, 786, 704, 583, 383, 979, 759, 966, 830, 771, 735, 43, 695, 390, 466, 401, 923, 902, 382, 124, 54, 985, 345, 154, 455, 13, 685, 565, 419, 720, 876, 643, 222, 489, 680, 870, 941, 764, 322, 572, 424, 779, 22, 602, 67, 136, 843, 210, 289, 306, 812, 356, 995, 981, 490, 462, 400, 315, 124, 958, 374, 644, 530, 608, 625, 648, 402, 287, 418, 208, 204, 302, 396, 614, 470, 955, 149, 814, 34, 67, 777, 147, 125, 454, 448, 386, 584, 579, 665, 141, 557, 236, 575, 187, 984, 777, 885, 774, 536, 581, 653, 443, 860, 163, 640, 988, 742, 259, 43, 933, 344, 955, 624, 593, 772, 303, 170, 857, 159, 11]
print('Before MergeSort: ', mylist)
MergeSort(mylist)
print('After MergeSort: ', mylist)
mylist = [251, 116, 369, 395, 791, 226, 862, 318, 90, 273, 686, 406, 867, 237, 418, 324, 624, 41, 29, 823, 891, 530, 565, 5, 931, 792, 143, 27, 646, 474, 698, 988, 93, 333, 998, 795, 399, 584, 491, 293, 851, 680, 664, 666, 116, 846, 79, 827, 498, 472, 616, 443, 439, 261, 272, 952, 967, 297, 332, 471, 601, 434, 707, 35, 863, 186, 352, 310, 400, 345, 554, 46, 320, 803, 964, 73, 138, 764, 459, 466, 456, 802, 302, 429, 911, 98, 588, 824, 472, 557, 46, 126, 645, 17, 61, 830, 41, 238, 929, 204, 281, 131, 178, 908, 268, 716, 909, 835, 239, 234, 597, 689, 487, 807, 853, 20, 829, 619, 986, 159, 68, 940, 222, 725, 632, 400, 364, 361, 249, 175, 827, 993, 485, 517, 13, 611, 898, 68, 62, 51, 912, 4, 800, 337, 123, 255, 420, 780, 478, 292, 592, 804, 43, 151, 187, 256, 943, 269, 11, 55, 581, 696, 509, 930, 688, 967, 922, 145, 401, 624, 52, 858, 610, 895, 648, 206, 713, 337, 736, 942, 762, 369, 992, 521, 612, 937, 482, 738, 196, 763, 151, 198, 381, 957, 686, 562, 928, 342, 846, 210, 250, 924, 702, 143, 317, 178, 386, 609, 310, 29, 89, 956, 553, 54, 509, 239, 826, 13, 790, 395, 234, 46, 537, 538, 528, 147, 841, 692, 752, 846, 354, 260, 477, 218, 394, 674, 604, 975, 147, 879, 6, 409, 474, 502, 212, 296, 404, 163, 815, 355, 888, 716, 15, 795, 722, 845, 525, 227, 69, 726, 727, 487, 626, 324, 352, 61, 519, 896, 831, 261, 310, 252, 473, 358, 818, 404, 859, 863, 412, 155, 300, 277, 629, 55, 398, 394, 934, 615, 68, 892, 587, 237, 10, 994, 370, 71, 261, 195, 588, 439, 214, 796, 870, 913, 544, 619, 487, 310, 515, 209, 44, 810, 11, 114, 314, 442, 422, 497, 957, 222, 909, 96, 494, 650, 921, 12, 739, 652, 355, 970, 166, 991, 308, 590, 835, 719, 494, 339, 347, 417, 994, 587, 75, 166, 292, 563, 673, 224, 748, 984, 249, 584, 730, 725, 459, 509, 573, 156, 2, 430, 490, 417, 71, 777, 117, 829, 177, 402, 315, 947, 654, 326, 327, 64, 529, 298, 796, 948, 966, 817, 49, 553, 931, 934, 968, 765, 828, 805, 916, 353, 972, 884, 905, 640, 259, 894, 410, 151, 778, 702, 309, 907, 983, 159, 330, 621, 696, 695, 700, 432, 713, 788, 692, 174, 677, 214, 881, 888, 513, 328, 584, 76, 645, 999, 527, 855, 977, 474, 656, 873, 725, 146, 406, 442, 135, 290, 676, 631, 436, 314, 889, 951, 308, 982, 4, 778, 592, 684, 92, 820, 616, 40, 188, 837, 216, 728, 213, 257, 546, 907, 345, 487, 837, 19, 973, 53, 896, 24, 470, 611, 133, 873, 440, 221, 116, 123, 153, 113, 177, 735, 593, 379, 530, 219, 157, 801, 997, 902, 716, 164, 684, 638, 748, 129, 630, 14, 191, 517, 95, 267, 925, 872, 427, 847, 666, 562, 732, 143, 859, 22, 172, 297, 958, 17, 813, 237, 723, 910, 355, 988, 77, 232, 964, 965, 156, 432, 949, 173, 315, 257, 870, 123, 116, 26, 423, 420, 192, 564, 320, 725, 353, 710, 263, 965, 456, 55, 141, 492, 818, 179, 187, 685, 64, 52, 827, 337, 370, 35, 542, 474, 572, 958, 600, 73, 870, 633, 973, 488, 7, 332, 838, 618, 929, 70, 971, 743, 247, 537, 179, 14, 313, 370, 963, 262, 531, 705, 201, 134, 114, 133, 327, 807, 751, 613, 778, 756, 605, 679, 400, 847, 865, 129, 487, 233, 356, 495, 196, 948, 501, 51, 670, 131, 611, 292, 345, 67, 484, 868, 46, 566, 41, 13, 964, 853, 763, 44, 824, 240, 315, 706, 894, 366, 60, 230, 777, 916, 733, 928, 465, 755, 654, 449, 615, 275, 421, 562, 467, 645, 504, 75, 257, 824, 609, 945, 513, 448, 842, 929, 928, 861, 58, 924, 60, 112, 157, 451, 860, 756, 22, 919, 727, 965, 550, 88, 144, 74, 655, 737, 252, 15, 850, 409, 239, 625, 816, 479, 304, 30, 541, 312, 904, 862, 420, 253, 330, 416, 209, 530, 366, 631, 217, 281, 130, 664, 892, 960, 364, 631, 56, 611, 855, 103, 51, 407, 76, 748, 792, 489, 907, 574, 721, 559, 7, 488, 18, 3, 344, 625, 556, 300, 150, 98, 486, 104, 370, 885, 249, 129, 739, 559, 589, 677, 50, 848, 952, 181, 983, 90, 496, 815, 150, 932, 880, 837, 400, 45, 910, 173, 245, 68, 869, 810, 108, 269, 348, 510, 676, 590, 312, 931, 911, 399, 273, 355, 21, 761, 759, 147, 816, 19, 619, 718, 192, 782, 139, 931, 232, 967, 664, 938, 260, 183, 369, 524, 531, 214, 223, 702, 993, 904, 756, 388, 712, 644, 925, 32, 869, 554, 600, 228, 463, 991, 25, 476, 514, 405, 608, 387, 602, 909, 334, 948, 458, 840, 600, 109, 581, 238, 159, 175, 572, 885, 891, 68, 672, 556, 835, 318, 916, 252, 818, 178, 433, 94, 505, 825, 601, 626, 155, 604, 636, 213, 93, 418, 933, 807, 430, 147, 48, 764, 929, 717, 129, 808, 575, 411, 771, 254, 448, 391, 724, 765, 64, 504, 171, 770, 893, 796, 952, 36, 818, 258, 282, 655, 27, 420, 342, 635, 661, 934, 890, 688, 776, 24, 970, 32, 905, 518, 493, 42, 932, 184, 300, 55, 109, 789, 994, 40, 454, 111, 689, 643, 821, 104, 94, 870, 635, 704, 422, 214, 351, 50, 130, 473, 167, 415, 873, 418, 736, 412, 699, 531, 902, 645, 777, 754, 665, 931, 84, 55, 982, 179, 698, 748, 842, 166, 188, 889, 620, 33, 794, 707, 747, 310, 724, 417, 432, 534, 966, 32, 909, 176, 936, 999, 676, 599, 207, 473, 793, 209, 565, 59, 457, 558, 627, 37, 908, 141, 449, 387, 298, 621, 527, 490, 381, 829, 424, 157, 735, 889, 800, 181, 652, 426, 326, 203, 413, 957, 916, 997]
print('Before QuickSort: ', mylist)
QuickSort(mylist)
print('After QuickSort: ', mylist)

# ----- test vectors -----
'''
Before MergeSort:  [666, 223, 32, 724, 428, 893, 998, 910, 964, 853, 264, 955, 495, 191, 825, 879, 56, 544, 455, 611, 453, 926, 39, 845, 468, 3, 785, 513, 568, 108, 642, 817, 385, 136, 838, 30, 824, 768, 584, 387, 286, 25, 793, 552, 189, 40, 910, 880, 842, 189, 15, 425, 364, 757, 58, 828, 180, 386, 421, 189, 808, 877, 995, 414, 863, 66, 954, 826, 241, 36, 584, 553, 837, 812, 56, 617, 32, 486, 33, 116, 117, 393, 84, 215, 472, 268, 529, 862, 717, 880, 762, 482, 895, 418, 864, 237, 846, 72, 827, 324, 732, 280, 77, 945, 693, 825, 74, 597, 752, 553, 95, 428, 685, 711, 460, 265, 896, 630, 155, 919, 999, 375, 777, 567, 362, 8, 663, 98, 771, 954, 712, 877, 825, 829, 274, 40, 111, 541, 111, 832, 287, 302, 902, 617, 934, 230, 747, 766, 694, 255, 593, 863, 544, 585, 326, 835, 638, 394, 60, 504, 428, 730, 821, 92, 584, 61, 648, 815, 728, 222, 275, 155, 619, 587, 462, 480, 885, 918, 200, 492, 840, 107, 508, 385, 390, 66, 235, 967, 848, 421, 452, 966, 502, 936, 972, 476, 104, 209, 23, 661, 86, 309, 839, 509, 650, 406, 974, 329, 853, 575, 173, 326, 492, 411, 699, 91, 226, 217, 602, 53, 101, 104, 927, 23, 514, 255, 852, 495, 655, 566, 41, 703, 135, 807, 368, 601, 580, 876, 897, 819, 655, 837, 779, 812, 240, 999, 124, 134, 963, 916, 319, 138, 175, 18, 975, 872, 921, 628, 827, 375, 149, 466, 471, 107, 866, 16, 762, 270, 732, 655, 974, 136, 986, 684, 602, 875, 293, 384, 360, 459, 50, 399, 144, 86, 555, 402, 480, 925, 992, 438, 681, 38, 553, 32, 20, 488, 470, 147, 530, 780, 330, 39, 985, 622, 464, 894, 541, 745, 947, 144, 863, 362, 510, 655, 558, 551, 453, 332, 80, 563, 19, 157, 597, 471, 871, 947, 870, 954, 215, 354, 88, 242, 837, 692, 260, 500, 266, 450, 696, 807, 806, 996, 900, 574, 706, 860, 258, 470, 832, 728, 546, 537, 255, 275, 728, 593, 254, 576, 811, 359, 196, 380, 871, 768, 464, 87, 644, 216, 226, 429, 251, 501, 507, 152, 853, 152, 724, 940, 477, 31, 376, 493, 264, 397, 180, 26, 823, 914, 264, 348, 876, 658, 456, 289, 111, 587, 134, 972, 469, 477, 136, 345, 130, 269, 682, 534, 72, 920, 805, 366, 520, 994, 872, 515, 809, 346, 358, 623, 826, 22, 3, 182, 684, 166, 813, 609, 606, 922, 669, 553, 305, 610, 272, 632, 688, 690, 196, 459, 885, 560, 979, 44, 386, 163, 563, 355, 34, 133, 757, 537, 177, 940, 649, 59, 8, 733, 72, 636, 392, 21, 536, 780, 802, 999, 495, 667, 494, 489, 540, 859, 991, 494, 919, 260, 314, 610, 442, 381, 945, 982, 212, 650, 973, 195, 211, 160, 527, 655, 811, 303, 663, 349, 327, 782, 169, 179, 356, 477, 736, 729, 415, 187, 598, 430, 935, 23, 109, 236, 743, 726, 500, 403, 116, 735, 558, 819, 253, 655, 737, 264, 76, 212, 491, 755, 660, 805, 830, 452, 503, 42, 23, 340, 572, 236, 450, 455, 910, 245, 985, 444, 874, 522, 247, 778, 92, 348, 863, 120, 294, 78, 351, 728, 349, 504, 455, 421, 685, 455, 777, 567, 465, 562, 65, 111, 725, 23, 881, 427, 605, 153, 878, 269, 259, 415, 152, 674, 396, 515, 753, 596, 106, 824, 31, 651, 724, 364, 791, 418, 588, 860, 424, 470, 96, 487, 571, 938, 493, 319, 373, 662, 662, 577, 753, 287, 762, 851, 359, 948, 136, 535, 454, 811, 789, 242, 615, 767, 388, 876, 261, 373, 392, 823, 268, 250, 971, 210, 590, 452, 429, 130, 878, 842, 236, 193, 269, 508, 730, 704, 811, 800, 937, 635, 542, 908, 187, 513, 372, 781, 86, 339, 90, 829, 25, 410, 28, 424, 392, 506, 701, 507, 300, 197, 225, 186, 313, 39, 947, 810, 819, 765, 430, 14, 644, 147, 187, 127, 457, 65, 566, 428, 309, 378, 965, 928, 758, 597, 990, 686, 900, 794, 74, 970, 256, 104, 894, 820, 740, 557, 454, 325, 548, 473, 967, 72, 533, 354, 101, 210, 499, 816, 52, 600, 954, 281, 575, 415, 499, 46, 286, 396, 684, 312, 138, 783, 196, 492, 536, 496, 863, 278, 902, 678, 527, 807, 355, 70, 580, 751, 37, 230, 999, 945, 954, 981, 167, 199, 973, 780, 564, 762, 357, 935, 912, 726, 84, 234, 794, 490, 241, 441, 401, 928, 372, 271, 82, 273, 733, 729, 602, 235, 775, 769, 450, 955, 984, 45, 124, 273, 537, 217, 636, 797, 582, 406, 232, 455, 917, 13, 547, 839, 128, 566, 916, 477, 642, 317, 828, 428, 347, 880, 614, 801, 149, 536, 576, 615, 77, 178, 503, 503, 171, 792, 228, 996, 52, 468, 205, 768, 580, 721, 678, 329, 397, 277, 861, 389, 988, 732, 569, 235, 412, 892, 40, 937, 493, 989, 995, 349, 751, 193, 272, 15, 171, 779, 41, 327, 183, 99, 457, 171, 548, 352, 760, 481, 515, 983, 305, 567, 806, 250, 472, 896, 340, 754, 26, 832, 806, 663, 511, 380, 385, 191, 285, 676, 153, 447, 281, 267, 428, 688, 875, 786, 704, 583, 383, 979, 759, 966, 830, 771, 735, 43, 695, 390, 466, 401, 923, 902, 382, 124, 54, 985, 345, 154, 455, 13, 685, 565, 419, 720, 876, 643, 222, 489, 680, 870, 941, 764, 322, 572, 424, 779, 22, 602, 67, 136, 843, 210, 289, 306, 812, 356, 995, 981, 490, 462, 400, 315, 124, 958, 374, 644, 530, 608, 625, 648, 402, 287, 418, 208, 204, 302, 396, 614, 470, 955, 149, 814, 34, 67, 777, 147, 125, 454, 448, 386, 584, 579, 665, 141, 557, 236, 575, 187, 984, 777, 885, 774, 536, 581, 653, 443, 860, 163, 640, 988, 742, 259, 43, 933, 344, 955, 624, 593, 772, 303, 170, 857, 159, 11]
After MergeSort:  [3, 3, 8, 8, 11, 13, 13, 14, 15, 15, 16, 18, 19, 20, 21, 22, 22, 23, 23, 23, 23, 23, 25, 25, 26, 26, 28, 30, 31, 31, 32, 32, 32, 33, 34, 34, 36, 37, 38, 39, 39, 39, 40, 40, 40, 41, 41, 42, 43, 43, 44, 45, 46, 50, 52, 52, 53, 54, 56, 56, 58, 59, 60, 61, 65, 65, 66, 66, 67, 67, 70, 72, 72, 72, 72, 74, 74, 76, 77, 77, 78, 80, 82, 84, 84, 86, 86, 86, 87, 88, 90, 91, 92, 92, 95, 96, 98, 99, 101, 101, 104, 104, 104, 106, 107, 107, 108, 109, 111, 111, 111, 111, 116, 116, 117, 120, 124, 124, 124, 124, 125, 127, 128, 130, 130, 133, 134, 134, 135, 136, 136, 136, 136, 136, 138, 138, 141, 144, 144, 147, 147, 147, 149, 149, 149, 152, 152, 152, 153, 153, 154, 155, 155, 157, 159, 160, 163, 163, 166, 167, 169, 170, 171, 171, 171, 173, 175, 177, 178, 179, 180, 180, 182, 183, 186, 187, 187, 187, 187, 189, 189, 189, 191, 191, 193, 193, 195, 196, 196, 196, 197, 199, 200, 204, 205, 208, 209, 210, 210, 210, 211, 212, 212, 215, 215, 216, 217, 217, 222, 222, 223, 225, 226, 226, 228, 230, 230, 232, 234, 235, 235, 235, 236, 236, 236, 236, 237, 240, 241, 241, 242, 242, 245, 247, 250, 250, 251, 253, 254, 255, 255, 255, 256, 258, 259, 259, 260, 260, 261, 264, 264, 264, 264, 265, 266, 267, 268, 268, 269, 269, 269, 270, 271, 272, 272, 273, 273, 274, 275, 275, 277, 278, 280, 281, 281, 285, 286, 286, 287, 287, 287, 289, 289, 293, 294, 300, 302, 302, 303, 303, 305, 305, 306, 309, 309, 312, 313, 314, 315, 317, 319, 319, 322, 324, 325, 326, 326, 327, 327, 329, 329, 330, 332, 339, 340, 340, 344, 345, 345, 346, 347, 348, 348, 349, 349, 349, 351, 352, 354, 354, 355, 355, 356, 356, 357, 358, 359, 359, 360, 362, 362, 364, 364, 366, 368, 372, 372, 373, 373, 374, 375, 375, 376, 378, 380, 380, 381, 382, 383, 384, 385, 385, 385, 386, 386, 386, 387, 388, 389, 390, 390, 392, 392, 392, 393, 394, 396, 396, 396, 397, 397, 399, 400, 401, 401, 402, 402, 403, 406, 406, 410, 411, 412, 414, 415, 415, 415, 418, 418, 418, 419, 421, 421, 421, 424, 424, 424, 425, 427, 428, 428, 428, 428, 428, 428, 429, 429, 430, 430, 438, 441, 442, 443, 444, 447, 448, 450, 450, 450, 452, 452, 452, 453, 453, 454, 454, 454, 455, 455, 455, 455, 455, 455, 456, 457, 457, 459, 459, 460, 462, 462, 464, 464, 465, 466, 466, 468, 468, 469, 470, 470, 470, 470, 471, 471, 472, 472, 473, 476, 477, 477, 477, 477, 480, 480, 481, 482, 486, 487, 488, 489, 489, 490, 490, 491, 492, 492, 492, 493, 493, 493, 494, 494, 495, 495, 495, 496, 499, 499, 500, 500, 501, 502, 503, 503, 503, 504, 504, 506, 507, 507, 508, 508, 509, 510, 511, 513, 513, 514, 515, 515, 515, 520, 522, 527, 527, 529, 530, 530, 533, 534, 535, 536, 536, 536, 536, 537, 537, 537, 540, 541, 541, 542, 544, 544, 546, 547, 548, 548, 551, 552, 553, 553, 553, 553, 555, 557, 557, 558, 558, 560, 562, 563, 563, 564, 565, 566, 566, 566, 567, 567, 567, 568, 569, 571, 572, 572, 574, 575, 575, 575, 576, 576, 577, 579, 580, 580, 580, 581, 582, 583, 584, 584, 584, 584, 585, 587, 587, 588, 590, 593, 593, 593, 596, 597, 597, 597, 598, 600, 601, 602, 602, 602, 602, 605, 606, 608, 609, 610, 610, 611, 614, 614, 615, 615, 617, 617, 619, 622, 623, 624, 625, 628, 630, 632, 635, 636, 636, 638, 640, 642, 642, 643, 644, 644, 644, 648, 648, 649, 650, 650, 651, 653, 655, 655, 655, 655, 655, 655, 658, 660, 661, 662, 662, 663, 663, 663, 665, 666, 667, 669, 674, 676, 678, 678, 680, 681, 682, 684, 684, 684, 685, 685, 685, 686, 688, 688, 690, 692, 693, 694, 695, 696, 699, 701, 703, 704, 704, 706, 711, 712, 717, 720, 721, 724, 724, 724, 725, 726, 726, 728, 728, 728, 728, 729, 729, 730, 730, 732, 732, 732, 733, 733, 735, 735, 736, 737, 740, 742, 743, 745, 747, 751, 751, 752, 753, 753, 754, 755, 757, 757, 758, 759, 760, 762, 762, 762, 762, 764, 765, 766, 767, 768, 768, 768, 769, 771, 771, 772, 774, 775, 777, 777, 777, 777, 778, 779, 779, 779, 780, 780, 780, 781, 782, 783, 785, 786, 789, 791, 792, 793, 794, 794, 797, 800, 801, 802, 805, 805, 806, 806, 806, 807, 807, 807, 808, 809, 810, 811, 811, 811, 811, 812, 812, 812, 813, 814, 815, 816, 817, 819, 819, 819, 820, 821, 823, 823, 824, 824, 825, 825, 825, 826, 826, 827, 827, 828, 828, 829, 829, 830, 830, 832, 832, 832, 835, 837, 837, 837, 838, 839, 839, 840, 842, 842, 843, 845, 846, 848, 851, 852, 853, 853, 853, 857, 859, 860, 860, 860, 861, 862, 863, 863, 863, 863, 863, 864, 866, 870, 870, 871, 871, 872, 872, 874, 875, 875, 876, 876, 876, 876, 877, 877, 878, 878, 879, 880, 880, 880, 881, 885, 885, 885, 892, 893, 894, 894, 895, 896, 896, 897, 900, 900, 902, 902, 902, 908, 910, 910, 910, 912, 914, 916, 916, 917, 918, 919, 919, 920, 921, 922, 923, 925, 926, 927, 928, 928, 933, 934, 935, 935, 936, 937, 937, 938, 940, 940, 941, 945, 945, 945, 947, 947, 947, 948, 954, 954, 954, 954, 954, 955, 955, 955, 955, 958, 963, 964, 965, 966, 966, 967, 967, 970, 971, 972, 972, 973, 973, 974, 974, 975, 979, 979, 981, 981, 982, 983, 984, 984, 985, 985, 985, 986, 988, 988, 989, 990, 991, 992, 994, 995, 995, 995, 996, 996, 998, 999, 999, 999, 999]
Before QuickSort:  [251, 116, 369, 395, 791, 226, 862, 318, 90, 273, 686, 406, 867, 237, 418, 324, 624, 41, 29, 823, 891, 530, 565, 5, 931, 792, 143, 27, 646, 474, 698, 988, 93, 333, 998, 795, 399, 584, 491, 293, 851, 680, 664, 666, 116, 846, 79, 827, 498, 472, 616, 443, 439, 261, 272, 952, 967, 297, 332, 471, 601, 434, 707, 35, 863, 186, 352, 310, 400, 345, 554, 46, 320, 803, 964, 73, 138, 764, 459, 466, 456, 802, 302, 429, 911, 98, 588, 824, 472, 557, 46, 126, 645, 17, 61, 830, 41, 238, 929, 204, 281, 131, 178, 908, 268, 716, 909, 835, 239, 234, 597, 689, 487, 807, 853, 20, 829, 619, 986, 159, 68, 940, 222, 725, 632, 400, 364, 361, 249, 175, 827, 993, 485, 517, 13, 611, 898, 68, 62, 51, 912, 4, 800, 337, 123, 255, 420, 780, 478, 292, 592, 804, 43, 151, 187, 256, 943, 269, 11, 55, 581, 696, 509, 930, 688, 967, 922, 145, 401, 624, 52, 858, 610, 895, 648, 206, 713, 337, 736, 942, 762, 369, 992, 521, 612, 937, 482, 738, 196, 763, 151, 198, 381, 957, 686, 562, 928, 342, 846, 210, 250, 924, 702, 143, 317, 178, 386, 609, 310, 29, 89, 956, 553, 54, 509, 239, 826, 13, 790, 395, 234, 46, 537, 538, 528, 147, 841, 692, 752, 846, 354, 260, 477, 218, 394, 674, 604, 975, 147, 879, 6, 409, 474, 502, 212, 296, 404, 163, 815, 355, 888, 716, 15, 795, 722, 845, 525, 227, 69, 726, 727, 487, 626, 324, 352, 61, 519, 896, 831, 261, 310, 252, 473, 358, 818, 404, 859, 863, 412, 155, 300, 277, 629, 55, 398, 394, 934, 615, 68, 892, 587, 237, 10, 994, 370, 71, 261, 195, 588, 439, 214, 796, 870, 913, 544, 619, 487, 310, 515, 209, 44, 810, 11, 114, 314, 442, 422, 497, 957, 222, 909, 96, 494, 650, 921, 12, 739, 652, 355, 970, 166, 991, 308, 590, 835, 719, 494, 339, 347, 417, 994, 587, 75, 166, 292, 563, 673, 224, 748, 984, 249, 584, 730, 725, 459, 509, 573, 156, 2, 430, 490, 417, 71, 777, 117, 829, 177, 402, 315, 947, 654, 326, 327, 64, 529, 298, 796, 948, 966, 817, 49, 553, 931, 934, 968, 765, 828, 805, 916, 353, 972, 884, 905, 640, 259, 894, 410, 151, 778, 702, 309, 907, 983, 159, 330, 621, 696, 695, 700, 432, 713, 788, 692, 174, 677, 214, 881, 888, 513, 328, 584, 76, 645, 999, 527, 855, 977, 474, 656, 873, 725, 146, 406, 442, 135, 290, 676, 631, 436, 314, 889, 951, 308, 982, 4, 778, 592, 684, 92, 820, 616, 40, 188, 837, 216, 728, 213, 257, 546, 907, 345, 487, 837, 19, 973, 53, 896, 24, 470, 611, 133, 873, 440, 221, 116, 123, 153, 113, 177, 735, 593, 379, 530, 219, 157, 801, 997, 902, 716, 164, 684, 638, 748, 129, 630, 14, 191, 517, 95, 267, 925, 872, 427, 847, 666, 562, 732, 143, 859, 22, 172, 297, 958, 17, 813, 237, 723, 910, 355, 988, 77, 232, 964, 965, 156, 432, 949, 173, 315, 257, 870, 123, 116, 26, 423, 420, 192, 564, 320, 725, 353, 710, 263, 965, 456, 55, 141, 492, 818, 179, 187, 685, 64, 52, 827, 337, 370, 35, 542, 474, 572, 958, 600, 73, 870, 633, 973, 488, 7, 332, 838, 618, 929, 70, 971, 743, 247, 537, 179, 14, 313, 370, 963, 262, 531, 705, 201, 134, 114, 133, 327, 807, 751, 613, 778, 756, 605, 679, 400, 847, 865, 129, 487, 233, 356, 495, 196, 948, 501, 51, 670, 131, 611, 292, 345, 67, 484, 868, 46, 566, 41, 13, 964, 853, 763, 44, 824, 240, 315, 706, 894, 366, 60, 230, 777, 916, 733, 928, 465, 755, 654, 449, 615, 275, 421, 562, 467, 645, 504, 75, 257, 824, 609, 945, 513, 448, 842, 929, 928, 861, 58, 924, 60, 112, 157, 451, 860, 756, 22, 919, 727, 965, 550, 88, 144, 74, 655, 737, 252, 15, 850, 409, 239, 625, 816, 479, 304, 30, 541, 312, 904, 862, 420, 253, 330, 416, 209, 530, 366, 631, 217, 281, 130, 664, 892, 960, 364, 631, 56, 611, 855, 103, 51, 407, 76, 748, 792, 489, 907, 574, 721, 559, 7, 488, 18, 3, 344, 625, 556, 300, 150, 98, 486, 104, 370, 885, 249, 129, 739, 559, 589, 677, 50, 848, 952, 181, 983, 90, 496, 815, 150, 932, 880, 837, 400, 45, 910, 173, 245, 68, 869, 810, 108, 269, 348, 510, 676, 590, 312, 931, 911, 399, 273, 355, 21, 761, 759, 147, 816, 19, 619, 718, 192, 782, 139, 931, 232, 967, 664, 938, 260, 183, 369, 524, 531, 214, 223, 702, 993, 904, 756, 388, 712, 644, 925, 32, 869, 554, 600, 228, 463, 991, 25, 476, 514, 405, 608, 387, 602, 909, 334, 948, 458, 840, 600, 109, 581, 238, 159, 175, 572, 885, 891, 68, 672, 556, 835, 318, 916, 252, 818, 178, 433, 94, 505, 825, 601, 626, 155, 604, 636, 213, 93, 418, 933, 807, 430, 147, 48, 764, 929, 717, 129, 808, 575, 411, 771, 254, 448, 391, 724, 765, 64, 504, 171, 770, 893, 796, 952, 36, 818, 258, 282, 655, 27, 420, 342, 635, 661, 934, 890, 688, 776, 24, 970, 32, 905, 518, 493, 42, 932, 184, 300, 55, 109, 789, 994, 40, 454, 111, 689, 643, 821, 104, 94, 870, 635, 704, 422, 214, 351, 50, 130, 473, 167, 415, 873, 418, 736, 412, 699, 531, 902, 645, 777, 754, 665, 931, 84, 55, 982, 179, 698, 748, 842, 166, 188, 889, 620, 33, 794, 707, 747, 310, 724, 417, 432, 534, 966, 32, 909, 176, 936, 999, 676, 599, 207, 473, 793, 209, 565, 59, 457, 558, 627, 37, 908, 141, 449, 387, 298, 621, 527, 490, 381, 829, 424, 157, 735, 889, 800, 181, 652, 426, 326, 203, 413, 957, 916, 997]
After QuickSort:  [2, 3, 4, 4, 5, 6, 7, 7, 10, 11, 11, 12, 13, 13, 13, 14, 14, 15, 15, 17, 17, 18, 19, 19, 20, 21, 22, 22, 24, 24, 25, 26, 27, 27, 29, 29, 30, 32, 32, 32, 33, 35, 35, 36, 37, 40, 40, 41, 41, 41, 42, 43, 44, 44, 45, 46, 46, 46, 46, 48, 49, 50, 50, 51, 51, 51, 52, 52, 53, 54, 55, 55, 55, 55, 55, 56, 58, 59, 60, 60, 61, 61, 62, 64, 64, 64, 67, 68, 68, 68, 68, 68, 69, 70, 71, 71, 73, 73, 74, 75, 75, 76, 76, 77, 79, 84, 88, 89, 90, 90, 92, 93, 93, 94, 94, 95, 96, 98, 98, 103, 104, 104, 108, 109, 109, 111, 112, 113, 114, 114, 116, 116, 116, 116, 117, 123, 123, 123, 126, 129, 129, 129, 129, 130, 130, 131, 131, 133, 133, 134, 135, 138, 139, 141, 141, 143, 143, 143, 144, 145, 146, 147, 147, 147, 147, 150, 150, 151, 151, 151, 153, 155, 155, 156, 156, 157, 157, 157, 159, 159, 159, 163, 164, 166, 166, 166, 167, 171, 172, 173, 173, 174, 175, 175, 176, 177, 177, 178, 178, 178, 179, 179, 179, 181, 181, 183, 184, 186, 187, 187, 188, 188, 191, 192, 192, 195, 196, 196, 198, 201, 203, 204, 206, 207, 209, 209, 209, 210, 212, 213, 213, 214, 214, 214, 214, 216, 217, 218, 219, 221, 222, 222, 223, 224, 226, 227, 228, 230, 232, 232, 233, 234, 234, 237, 237, 237, 238, 238, 239, 239, 239, 240, 245, 247, 249, 249, 249, 250, 251, 252, 252, 252, 253, 254, 255, 256, 257, 257, 257, 258, 259, 260, 260, 261, 261, 261, 262, 263, 267, 268, 269, 269, 272, 273, 273, 275, 277, 281, 281, 282, 290, 292, 292, 292, 293, 296, 297, 297, 298, 298, 300, 300, 300, 302, 304, 308, 308, 309, 310, 310, 310, 310, 310, 312, 312, 313, 314, 314, 315, 315, 315, 317, 318, 318, 320, 320, 324, 324, 326, 326, 327, 327, 328, 330, 330, 332, 332, 333, 334, 337, 337, 337, 339, 342, 342, 344, 345, 345, 345, 347, 348, 351, 352, 352, 353, 353, 354, 355, 355, 355, 355, 356, 358, 361, 364, 364, 366, 366, 369, 369, 369, 370, 370, 370, 370, 379, 381, 381, 386, 387, 387, 388, 391, 394, 394, 395, 395, 398, 399, 399, 400, 400, 400, 400, 401, 402, 404, 404, 405, 406, 406, 407, 409, 409, 410, 411, 412, 412, 413, 415, 416, 417, 417, 417, 418, 418, 418, 420, 420, 420, 420, 421, 422, 422, 423, 424, 426, 427, 429, 430, 430, 432, 432, 432, 433, 434, 436, 439, 439, 440, 442, 442, 443, 448, 448, 449, 449, 451, 454, 456, 456, 457, 458, 459, 459, 463, 465, 466, 467, 470, 471, 472, 472, 473, 473, 473, 474, 474, 474, 474, 476, 477, 478, 479, 482, 484, 485, 486, 487, 487, 487, 487, 487, 488, 488, 489, 490, 490, 491, 492, 493, 494, 494, 495, 496, 497, 498, 501, 502, 504, 504, 505, 509, 509, 509, 510, 513, 513, 514, 515, 517, 517, 518, 519, 521, 524, 525, 527, 527, 528, 529, 530, 530, 530, 531, 531, 531, 534, 537, 537, 538, 541, 542, 544, 546, 550, 553, 553, 554, 554, 556, 556, 557, 558, 559, 559, 562, 562, 562, 563, 564, 565, 565, 566, 572, 572, 573, 574, 575, 581, 581, 584, 584, 584, 587, 587, 588, 588, 589, 590, 590, 592, 592, 593, 597, 599, 600, 600, 600, 601, 601, 602, 604, 604, 605, 608, 609, 609, 610, 611, 611, 611, 611, 612, 613, 615, 615, 616, 616, 618, 619, 619, 619, 620, 621, 621, 624, 624, 625, 625, 626, 626, 627, 629, 630, 631, 631, 631, 632, 633, 635, 635, 636, 638, 640, 643, 644, 645, 645, 645, 645, 646, 648, 650, 652, 652, 654, 654, 655, 655, 656, 661, 664, 664, 664, 665, 666, 666, 670, 672, 673, 674, 676, 676, 676, 677, 677, 679, 680, 684, 684, 685, 686, 686, 688, 688, 689, 689, 692, 692, 695, 696, 696, 698, 698, 699, 700, 702, 702, 702, 704, 705, 706, 707, 707, 710, 712, 713, 713, 716, 716, 716, 717, 718, 719, 721, 722, 723, 724, 724, 725, 725, 725, 725, 726, 727, 727, 728, 730, 732, 733, 735, 735, 736, 736, 737, 738, 739, 739, 743, 747, 748, 748, 748, 748, 751, 752, 754, 755, 756, 756, 756, 759, 761, 762, 763, 763, 764, 764, 765, 765, 770, 771, 776, 777, 777, 777, 778, 778, 778, 780, 782, 788, 789, 790, 791, 792, 792, 793, 794, 795, 795, 796, 796, 796, 800, 800, 801, 802, 803, 804, 805, 807, 807, 807, 808, 810, 810, 813, 815, 815, 816, 816, 817, 818, 818, 818, 818, 820, 821, 823, 824, 824, 824, 825, 826, 827, 827, 827, 828, 829, 829, 829, 830, 831, 835, 835, 835, 837, 837, 837, 838, 840, 841, 842, 842, 845, 846, 846, 846, 847, 847, 848, 850, 851, 853, 853, 855, 855, 858, 859, 859, 860, 861, 862, 862, 863, 863, 865, 867, 868, 869, 869, 870, 870, 870, 870, 872, 873, 873, 873, 879, 880, 881, 884, 885, 885, 888, 888, 889, 889, 889, 890, 891, 891, 892, 892, 893, 894, 894, 895, 896, 896, 898, 902, 902, 904, 904, 905, 905, 907, 907, 907, 908, 908, 909, 909, 909, 909, 910, 910, 911, 911, 912, 913, 916, 916, 916, 916, 919, 921, 922, 924, 924, 925, 925, 928, 928, 928, 929, 929, 929, 929, 930, 931, 931, 931, 931, 931, 932, 932, 933, 934, 934, 934, 936, 937, 938, 940, 942, 943, 945, 947, 948, 948, 948, 949, 951, 952, 952, 952, 956, 957, 957, 957, 958, 958, 960, 963, 964, 964, 964, 965, 965, 965, 966, 966, 967, 967, 967, 968, 970, 970, 971, 972, 973, 973, 975, 977, 982, 982, 983, 983, 984, 986, 988, 988, 991, 991, 992, 993, 993, 994, 994, 994, 997, 997, 998, 999, 999]
'''
