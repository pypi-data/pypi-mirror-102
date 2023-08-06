/**
 * create time : 2020-12-31
 * c_api.cc : Python wrapper for C++ implementation of FastSGG
 */
#include "Generation.hpp"
#include <Python.h>
using namespace std;
using namespace gl;

#ifdef __cplusplus
extern "C" {
#endif

PyObject* get_generation_ptr(PyObject* self, PyObject* args);
PyObject* start_generate(PyObject* self, PyObject* args);
PyObject* get_current_gentag(PyObject* self, PyObject* args);
PyObject* get_current_progress(PyObject* self, PyObject* args);
PyObject* is_generation_done(PyObject* self, PyObject* args);
PyObject* has_generation_start(PyObject* self, PyObject* args);
PyObject* get_actual_num_edges(PyObject* self, PyObject* args);

static PyMethodDef ModuleFunctions [] = {
    {"get_generation_ptr", get_generation_ptr, METH_VARARGS,
     "Get the pointer of a Generation Class instance"},

    {"start_generate", start_generate, METH_VARARGS,
     "Start generating graphs"},

    {"get_current_gentag", get_current_gentag, METH_VARARGS,
     "Get current node/edge generation information"},

    {"get_current_progress", get_current_progress, METH_VARARGS,
     "Get current generation progress"},

    {"is_generation_done", is_generation_done, METH_VARARGS,
     "Has the generation done."},

    {"has_generation_start", has_generation_start, METH_VARARGS,
     "Has the generation started."},

    {"get_actual_num_edges", get_actual_num_edges, METH_VARARGS,
     "Get the actual number of edges."},

    // All function listing must end with this value.
    {nullptr, nullptr, 0, nullptr}
};

// Module definition
static struct PyModuleDef ModuleDefinitions {
    PyModuleDef_HEAD_INIT,
    // Module name as string 
    "pyfastsgg",
    // Module documentation (docstring)
    "A simple C++ native-code FastSGG module for Python3.",
    -1,
    // Functions exposed to the module 
    ModuleFunctions
};

/** Module Initialization function: must have this name schema
 *  PyInit_<ModuleName> where ModuleName is the same base name of the 
 *  shared library ModuleName.so (on Linux) or ModuleName.pyd (on Windows)
 */
PyMODINIT_FUNC PyInit_pyfastsgg(void)
{
    Py_Initialize();
    PyObject* pModule = PyModule_Create(&ModuleDefinitions);
    PyModule_AddObject(pModule, "version", Py_BuildValue("s", "version 0.1.0-Alpha"));
    return pModule;
}
// =============== END REGISTERING ===============

// =============== Concrete Realization ==============

/**
 * [get_generation_ptr description]
 * @param  filename     [string]
 * @return Generation*  [pointer]
 */
PyObject* get_generation_ptr(PyObject* self, PyObject* args) {
    char *str;
    if (!PyArg_ParseTuple(args, "s", &str))
        Py_RETURN_NONE;
    string filename(str);
    fastsgg::Generation *gen_ptr = new fastsgg::Generation(filename);
    PyObject *rtn = PyLong_FromVoidPtr(gen_ptr);
    return rtn;
}

/**
 * [start_generate description]
 * @param  Generation* [pointer]
 * @return None
 */
PyObject* start_generate(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        Py_RETURN_NONE;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    gen_ptr->run();
    Py_RETURN_NONE;
}

/**
 * [get_current_gentag description]
 * @param  Generation*   [pointer]
 * @return Node/Edge-{}  [string]
 */
PyObject* get_current_gentag(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        Py_RETURN_NONE;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    string tag = gen_ptr->currentGenerationTag();
    PyObject *rtn = PyUnicode_FromString(tag.c_str());
    return rtn;
}

/**
 * [get_current_progress description]
 * @param  Generation*   [pointer]
 * @return progress      [double]
 */
PyObject* get_current_progress(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        Py_RETURN_NONE;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    double pg = gen_ptr->currentGenerationProgress();
    PyObject *rtn = PyFloat_FromDouble(pg);
    return rtn;
}

/**
 * [is_generation_done description]
 * @param  Generation*   [pointer]
 * @return isDone        [boolean]
 */
PyObject* is_generation_done(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        return Py_False;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    bool ans = gen_ptr->isGenerationDone();
    if (ans)
        return Py_True;
    return Py_False;
}

/**
 * [has_generation_start description]
 * @param  Generation*   [pointer]
 * @return hasStart      [boolean]
 */
PyObject* has_generation_start(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        return Py_False;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    bool ans = gen_ptr->hasGenerationStart();
    if (ans)
        return Py_True;
    return Py_False;
}

/**
 * [get_actual_num_edges description]
 * @param  Generation*   [pointer]
 * @param  edge label    [const char*]
 * @return num_edges     [int]
 */
PyObject* get_actual_num_edges(PyObject* self, PyObject* args) {
    PyObject* obj;
    char* ch_e_label;
    PyObject* zero = PyLong_FromLongLong(0);
    if (!PyArg_ParseTuple(args, "Os", &obj, &ch_e_label))
        return zero;
    void *vp = PyLong_AsVoidPtr(obj);
    fastsgg::Generation *gen_ptr = (fastsgg::Generation*)vp;
    std::string e_label(ch_e_label);
    fastsgg::int_t ans = gen_ptr->getActualEdges(e_label);
    PyObject* rtn = PyLong_FromLongLong(ans);
    return rtn;
}
// =============== END REALIZATION ===============

#ifdef __cplusplus
}
#endif