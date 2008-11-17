// Autogenerated AST node
package org.python.antlr.ast;
import org.python.antlr.PythonTree;
import org.antlr.runtime.CommonToken;
import org.antlr.runtime.Token;
import java.io.DataOutputStream;
import java.io.IOException;

public class Call extends exprType {
    public exprType func;
    public java.util.List<exprType> args;
    public java.util.List<keywordType> keywords;
    public exprType starargs;
    public exprType kwargs;

    private final static String[] fields = new String[] {"func", "args",
                                                          "keywords",
                                                          "starargs", "kwargs"};
    public String[] get_fields() { return fields; }

    public Call(exprType func, java.util.List<exprType> args,
    java.util.List<keywordType> keywords, exprType starargs, exprType kwargs) {
        this.func = func;
        addChild(func);
        this.args = args;
        if (args != null) {
            for(PythonTree t : args) {
                addChild(t);
            }
        }
        this.keywords = keywords;
        if (keywords != null) {
            for(PythonTree t : keywords) {
                addChild(t);
            }
        }
        this.starargs = starargs;
        addChild(starargs);
        this.kwargs = kwargs;
        addChild(kwargs);
    }

    public Call(Token token, exprType func, java.util.List<exprType> args,
    java.util.List<keywordType> keywords, exprType starargs, exprType kwargs) {
        super(token);
        this.func = func;
        addChild(func);
        this.args = args;
        if (args != null) {
            for(PythonTree t : args) {
                addChild(t);
            }
        }
        this.keywords = keywords;
        if (keywords != null) {
            for(PythonTree t : keywords) {
                addChild(t);
            }
        }
        this.starargs = starargs;
        addChild(starargs);
        this.kwargs = kwargs;
        addChild(kwargs);
    }

    public Call(int ttype, Token token, exprType func, java.util.List<exprType>
    args, java.util.List<keywordType> keywords, exprType starargs, exprType
    kwargs) {
        super(ttype, token);
        this.func = func;
        addChild(func);
        this.args = args;
        if (args != null) {
            for(PythonTree t : args) {
                addChild(t);
            }
        }
        this.keywords = keywords;
        if (keywords != null) {
            for(PythonTree t : keywords) {
                addChild(t);
            }
        }
        this.starargs = starargs;
        addChild(starargs);
        this.kwargs = kwargs;
        addChild(kwargs);
    }

    public Call(PythonTree tree, exprType func, java.util.List<exprType> args,
    java.util.List<keywordType> keywords, exprType starargs, exprType kwargs) {
        super(tree);
        this.func = func;
        addChild(func);
        this.args = args;
        if (args != null) {
            for(PythonTree t : args) {
                addChild(t);
            }
        }
        this.keywords = keywords;
        if (keywords != null) {
            for(PythonTree t : keywords) {
                addChild(t);
            }
        }
        this.starargs = starargs;
        addChild(starargs);
        this.kwargs = kwargs;
        addChild(kwargs);
    }

    public String toString() {
        return "Call";
    }

    public String toStringTree() {
        StringBuffer sb = new StringBuffer("Call(");
        sb.append("func=");
        sb.append(dumpThis(func));
        sb.append(",");
        sb.append("args=");
        sb.append(dumpThis(args));
        sb.append(",");
        sb.append("keywords=");
        sb.append(dumpThis(keywords));
        sb.append(",");
        sb.append("starargs=");
        sb.append(dumpThis(starargs));
        sb.append(",");
        sb.append("kwargs=");
        sb.append(dumpThis(kwargs));
        sb.append(",");
        sb.append(")");
        return sb.toString();
    }

    public <R> R accept(VisitorIF<R> visitor) throws Exception {
        return visitor.visitCall(this);
    }

    public void traverse(VisitorIF visitor) throws Exception {
        if (func != null)
            func.accept(visitor);
        if (args != null) {
            for (PythonTree t : args) {
                if (t != null)
                    t.accept(visitor);
            }
        }
        if (keywords != null) {
            for (PythonTree t : keywords) {
                if (t != null)
                    t.accept(visitor);
            }
        }
        if (starargs != null)
            starargs.accept(visitor);
        if (kwargs != null)
            kwargs.accept(visitor);
    }

    private int lineno = -1;
    public int getLineno() {
        if (lineno != -1) {
            return lineno;
        }
        return getLine();
    }

    public void setLineno(int num) {
        lineno = num;
    }

    private int col_offset = -1;
    public int getCol_offset() {
        if (col_offset != -1) {
            return col_offset;
        }
        return getCharPositionInLine();
    }

    public void setCol_offset(int num) {
        col_offset = num;
    }

}
