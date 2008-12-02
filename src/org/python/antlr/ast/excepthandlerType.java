// Autogenerated AST node
package org.python.antlr.ast;
import org.antlr.runtime.CommonToken;
import org.antlr.runtime.Token;
import org.python.antlr.PythonTree;
import org.python.antlr.adapter.AstAdapters;
import org.python.core.AstList;
import org.python.core.Py;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.core.PyType;
import org.python.expose.ExposedGet;
import org.python.expose.ExposedMethod;
import org.python.expose.ExposedNew;
import org.python.expose.ExposedSet;
import org.python.expose.ExposedType;

@ExposedType(name = "_ast.excepthandler", base = PyObject.class)
public abstract class excepthandlerType extends PythonTree {

    public static final PyType TYPE = PyType.fromClass(excepthandlerType.class);
    private final static String[] attributes = new String[] {"lineno",
                                                              "col_offset"};
@ExposedGet(name = "_attributes")
    public String[] get_attributes() { return attributes; }

    public excepthandlerType() {
    }

    public excepthandlerType(PyType subType) {
    }

    public excepthandlerType(int ttype, Token token) {
        super(ttype, token);
    }

    public excepthandlerType(Token token) {
        super(token);
    }

    public excepthandlerType(PythonTree node) {
        super(node);
    }

}
