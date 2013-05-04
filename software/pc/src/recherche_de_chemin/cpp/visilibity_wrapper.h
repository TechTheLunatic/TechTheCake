#ifndef POLYGON_H
#define POLYGON_H

#include "visilibity.hpp"
#include "table.h"

class VisilibityWrapper
{  
public:
    enum Exception
    {
        RETURN_OK,
        ENVIRONMENT_IS_NOT_VALID
    };

public:
    VisilibityWrapper(int width, int height);
    void epsilon(double e);
    void define_map_dimensions(int width, int height);
    void add_rectangle(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4);
    void add_circle(int x, int y, int radius);
    Exception build_environment();
    void reset_environment();
    VisiLibity::Polyline path(int x_start, int y_start, int x_end, int y_end);


private:
    double _epsilon;
    VisiLibity::Environment _environment;
    VisiLibity::Visibility_Graph _visibility_graph;
    Table _table;
};

#endif // POLYGON_H